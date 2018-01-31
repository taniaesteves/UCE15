#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extensions
import unidecode
import json
import datetime
import io
from pprint import pprint
import os
import re

try:
    to_unicode = unicode
except:
    to_unicode = str

def getmarkerimages(markerid, feature, markersinfo):
	imagelimit = 0
	imagedirpath = re.sub("\s+", "_", catalog_title.lower()) + '/figures'
	dirpath = '/home/atlas/AtlasInnovation/UCE15/Code/Model/Catalogs/' + imagedirpath		
	for imagefile in os.listdir(dirpath):				
		if imagefile.startswith(str(markerid) + '_' + feature + "_"):
			print(imagefile)
			if imagelimit > 20:
				break
			markersinfo["properties"]["IMAGES"].append(imagedirpath + "/" + imagefile)				
			imagelimit += 1

'''Create an encoder subclassing JSON.encoder. 
Make this encoder aware of our classes (e.g. datetime.datetime objects) 
'''
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

# DATABASE CONFIGURATION

dbname   = 'atlas'
user     = 'atlas'
host     = 'localhost'
password = ''

print("-------------- Actual DataBase Connection --------------\n")
print("       [dbname] = '" + dbname + "'")
print("       [user]   = '" + user + "'")
print("       [host]   = '" + host + "'\n")
print("--------------------------------------------------------\n")
print("Press <e> to edit ou <enter> to continue...")
option = input()

if (option == 'e' or option == 'E'):
	print("Enter dbname: ")
	dbname = input()
	print("Enter user: ")
	user = input()
	print("Enter host: ")
	host = input()
	print("Enter password: ")
	password = input()
	
try:
	conn = psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='" + host + "' password='" + password + "'")
except: 
	print("\nERROR: UNABLE TO CONNECT TO THE DATABASE")
	exit()

conn.set_client_encoding('LATIN-1')
cur = conn.cursor()

# CATALOG NAME

print("\nEnter catalog name:")
catalog_title = input()

try:
	cur.execute("SELECT id from catalog where title='" + catalog_title + "';")
except:
	print("\nERROR: UNABLE TO GET CATALOG ID")
	exit()

rows = cur.fetchall()

if rows == []:
	print("\nERROR: CATALOG NAME INVALID")
	exit()

catalog_id = rows[0][0]

print("catalog name: " + str(catalog_id))

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, cur)

print("encoding: " + conn.encoding)

try:
        cur.execute("SELECT id, code, title, icon FROM feature f JOIN catalog_feature cf ON f.id=cf.featureid WHERE cf.catalogid=" + str(catalog_id) + ";")
except:
	print("\nERROR: UNABLE TO GET FEATURES: ")
	exit()

print("row count: " +  str(cur.rowcount))

features = cur.fetchall()
featuresinfo = []

# ----------- ALL -----------

for feature in features:
	n_markers = 0

	# add feature to featuresinfo struct
	actualfeature = {
		"type": feature[1],
		"title": feature[2],
		"icon": feature[3],
		"delta": "All"
	}

	# feature file content struct
	featurecontent = {
		"type": "FeatureCollection",
		"features": []
	}

	# search feature's markers
	try:
		cur.execute(" SELECT id, latitude, longitude, imagepath, first_timestamp, precision, note, address FROM marker where featureid=" + str(feature[0]) + ";")
	except:
		print("\nERROR: UNABLE TO GET MARKERS")
		exit()

	markers = cur.fetchall()
	
	for marker in markers:
		# feature's markers
		actualfeatureinfo = {
			"type": "Feature",
			"id": marker[0],
			"properties": { 
				"TITLE": feature[1] + " - " + marker[7], 
				"TIMESTAMP": str(marker[4]), 
				"PRECISION": marker[5], 
				"NOTA": marker[6], 
				"IMAGES": [],
				"ADDRESS": marker[7]
			}, 
			"geometry": { 
				"type": "Point", 
				"coordinates": [ marker[2], marker[1]  ] 
			} 
		}		
		getmarkerimages(marker[0], feature[1], actualfeatureinfo)
		if len(actualfeatureinfo["properties"]["IMAGES"]) == 0:
			actualfeatureinfo["properties"]["IMAGES"] = [marker[3]]
		featurecontent["features"].append(actualfeatureinfo)
		n_markers += 1


	if n_markers > 0:
		featuresinfo.append(actualfeature)
		# Write JSON file
		featuremarkersfilename = unidecode.unidecode("/home/atlas/geojsons/" + feature[1] + ".geojson")
		with io.open(featuremarkersfilename, 'w', encoding='utf8') as outfile:
		    str_ = json.dumps(featurecontent, cls=Encoder,
		                      indent=4, sort_keys=True,
		                      separators=(',', ': '), ensure_ascii=False)
		    outfile.write(to_unicode(str_))
		print("\nFile '" + featuremarkersfilename + " created successfully!")	

# ----------- DELTA -----------
for feature in features:
	n_markers = 0

	# add feature to featuresinfo struct
	actualfeature = {
		"type": feature[1] + '_delta',
		"title": feature[2],
		"icon": feature[3],
		"delta": "LastMonth"
	}

	# feature file content struct
	featurecontent = {
		"type": "FeatureCollection",
		"features": []
	}

	# search: os marcadores que foram vistos pela ultima vez há mais de 15 dias (exceptos os novos marcadores):
	try:
		cur.execute("SELECT id, latitude, longitude, imagepath, first_timestamp, last_timestamp, precision, note, address \
					FROM marker \
					WHERE \
					featureid = " + str(feature[0]) + " \
					AND EXTRACT(YEAR FROM last_timestamp) = EXTRACT(YEAR FROM (CURRENT_DATE - INTERVAL '1 month')) \
					AND first_timestamp < CURRENT_DATE - INTERVAL '1 month' \
					AND last_timestamp < CURRENT_DATE - INTERVAL '15 days';")
	except:
		print("\nERROR: UNABLE TO GET REMOVED MARKERS")
		exit()

	markers = cur.fetchall()
	
	for marker in markers:
		# feature's markers
		actualfeatureinfo = {
			"type": "Feature",
			"id": marker[0],
			"properties": { 
				"TITLE": feature[1] + " - " + marker[8], 
				"TIMESTAMP": str(marker[5]), 
				"PRECISION": marker[6], 
				"NOTA": marker[7], 
				"IMAGES": [],
				"ADDRESS": marker[8],
				"DELTA": "removed"
			}, 
			"geometry": { 
				"type": "Point", 
				"coordinates": [ marker[2], marker[1]  ] 
			} 
		}
		getmarkerimages(marker[0], feature[1], actualfeatureinfo)
		if len(actualfeatureinfo["properties"]["IMAGES"]) == 0:
			actualfeatureinfo["properties"]["IMAGES"] = [marker[3]]
		featurecontent["features"].append(actualfeatureinfo)
		n_markers += 1

	# search: Novos marcadores (que foram vistos pela ultima vez nos ultimos 15 dias):
	try:
		cur.execute("SELECT id, latitude, longitude, imagepath, first_timestamp, last_timestamp, precision, note, address \
					FROM marker \
					WHERE \
					featureid = " + str(feature[0]) + " \
					AND first_timestamp > CURRENT_DATE - INTERVAL '1 month';")
					# AND last_timestamp >= CURRENT_DATE - INTERVAL '15 days';")
	except:
		print("\nERROR: UNABLE TO GET NEW MARKERS")
		exit()

	markers = cur.fetchall()
	
	for marker in markers:
		# feature's markers
		actualfeatureinfo = {
			"type": "Feature",
			"id": marker[0],
			"properties": { 
				"TITLE": feature[1] + " - " + marker[8], 
				"TIMESTAMP": str(marker[5]), 
				"PRECISION": marker[6], 
				"NOTA": marker[7], 
				"IMAGES": [],
				"ADDRESS": marker[8],
				"DELTA": "added"
			}, 
			"geometry": { 
				"type": "Point", 
				"coordinates": [ marker[2], marker[1]  ] 
			} 
		}
		getmarkerimages(marker[0], feature[1], actualfeatureinfo)
		if len(actualfeatureinfo["properties"]["IMAGES"]) == 0:
			actualfeatureinfo["properties"]["IMAGES"] = [marker[3]]
		featurecontent["features"].append(actualfeatureinfo)
		n_markers += 1

	if n_markers > 0:
		featuresinfo.append(actualfeature)
		# Write JSON file
		featuremarkersfilename = unidecode.unidecode("/home/atlas/geojsons/" + feature[1] + "_delta.geojson")
		with io.open(featuremarkersfilename, 'w', encoding='LATIN-1') as outfile:
		    str_ = json.dumps(featurecontent, cls=Encoder,
		                      indent=4, sort_keys=True,
		                      separators=(',', ': '), ensure_ascii=False)
		    outfile.write(to_unicode(str_))
		print("\nFile '" + featuremarkersfilename + " created successfully!")	



# Write JSON file
featuresfilename = unidecode.unidecode("/home/atlas/geojsons/featuresinfo.json")
with io.open(featuresfilename, 'w', encoding='LATIN-1') as outfile:
    str_ = json.dumps(featuresinfo,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
print("\nFile '" + featuresfilename + " created successfully!")
