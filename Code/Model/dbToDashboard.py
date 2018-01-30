#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extensions
import unidecode
import json
import datetime
import io
from pprint import pprint

try:
    to_unicode = unicode
except:
    to_unicode = str

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

for feature in features:

	# add feature to featuresinfo struct
	actualfeature = {
		"type": feature[1],
		"title": feature[2],
		"icon": feature[3]
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
				"IMAGE": marker[3],
				"ADDRESS": marker[7]
			}, 
			"geometry": { 
				"type": "Point", 
				"coordinates": [ marker[2], marker[1]  ] 
			} 
		}
		featurecontent["features"].append(actualfeatureinfo);


	if len(markers) > 0:
		featuresinfo.append(actualfeature)
		# Write JSON file
		featuremarkersfilename = unidecode.unidecode("/home/atlas/geojsons/" + feature[1] + ".geojson")
		with io.open(featuremarkersfilename, 'w', encoding='utf8') as outfile:
		    str_ = json.dumps(featurecontent, cls=Encoder,
		                      indent=4, sort_keys=True,
		                      separators=(',', ': '), ensure_ascii=False)
		    outfile.write(to_unicode(str_))
		print("\nFile '" + featuremarkersfilename + " created successfully!")	

# Write JSON file
featuresfilename = unidecode.unidecode("/home/atlas/geojsons/featuresinfo.json")
with io.open(featuresfilename, 'w', encoding='utf8') as outfile:
    str_ = json.dumps(featuresinfo,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
print("\nFile '" + featuresfilename + " created successfully!")
