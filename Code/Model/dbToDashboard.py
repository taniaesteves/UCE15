#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extensions
import unidecode
from pprint import pprint

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
        cur.execute("SELECT id, code, title, icon FROM feature f JOIN catalog_feature cf ON f.id=cf.featureid WHERE cf.catalogid=1;")
except:
	print("\nERROR: UNABLE TO GET FEATURES")
	exit()

print("row count: " +  str(cur.rowcount));

features = cur.fetchall()
featuresinfo = []

for feature in features:

	# add feature to featuresinfo struct
	actualfeature = {
		"type": feature[1],
		"icon": feature[3]
	}
	featuresinfo.append(actualfeature)

	# feature file content struct
	featurecontent = {
		"type": "FeatureCollection",
		"features": []
	}

	# search feature's markers
	try:
		cur.execute("SELECT m.id as markerid, latitude, longitude, imagepath, timestamp, precision, note \
					 FROM marker m JOIN feature f ON m.featureid=" + str(feature[0]) + ";")
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
				"TITLE": feature[2], 
				"TIMESTAMP": marker[4], 
				"PRECISION": marker[5], 
				"NOTA": marker[6], 
				"IMAGE": marker[3] 
			}, 
			"geometry": { 
				"type": "Point", 
				"coordinates": [ marker[2], marker[1]  ] 
			} 
		}
		featurecontent["features"].append(actualfeatureinfo);

	# Write JSON file
	featuremarkersfilename = unidecode.unidecode(feature[1] + ".geojson").lower()
	with io.open(featuremarkersfilename, 'wb', encoding='utf8') as outfile:
	    str_ = json.dumps(featurecontent,
	                      indent=4, sort_keys=True,
	                      separators=(',', ': '), ensure_ascii=False)
	    outfile.write(to_unicode(str_))
	print("\nFile '" + featuremarkersfile + " created successfully!")	

# Write JSON file
featuresfilename = unidecode.unidecode("featuresinfo.json")
with io.open(featuresfilename, 'wb', encoding='utf8') as outfile:
    str_ = json.dumps(featuresinfo,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
print("\nFile '" + featuresfilename + " created successfully!")
