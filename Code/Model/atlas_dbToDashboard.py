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

'''Create an encoder subclassing JSON.encoder. 
Make this encoder aware of our classes (e.g. datetime.datetime objects) 
'''
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

'''Get marker's images'''
def getmarkerimages(markerid, feature, markersinfo):
    imagelimit = 0
    imagedirpath = re.sub("\s+", "_", catalog_title.lower()) + '/figures'
    dirpath = '/home/atlas/AtlasInnovation/UCE15/Code/Model/Catalogs/' + imagedirpath
    imagesnames = os.listdir(dirpath)
    for imagefile in sorted(imagesnames, reverse=True):				
        if imagefile.startswith(str(markerid) + '_' + feature + "_"):
            # print(imagefile)
            if imagelimit > 19:
                break
            markersinfo["properties"]["IMAGES"].append(imagedirpath + "/" + imagefile)				
            imagelimit += 1

'''Get feature's markers'''
def getfeaturemarkers(features_array, delta, delta_type, query):
    for feature in features_array:
        n_markers = 0

        # add feature to featuresinfo struct
        if (delta == 'LastMonth'):
            actualfeature = {
                "type": feature[1] + '_delta',
                "title": feature[2],
                "icon": feature[3],
                "delta": delta
            }
        else:
            actualfeature = {
                "type": feature[1],
                "title": feature[2],
                "icon": feature[3],
                "delta": delta
            }

        # feature file content struct
        featurecontent = {
            "type": "FeatureCollection",
            "features": []
        }

        # search feature's markers
        try:
            print(feature[0])
            cur.execute(query, (feature[0],))
        except psycopg2.Error as e:
            print("\nERROR: UNABLE TO GET MARKERS [" + delta + "]: " + e) 
            exit()
        
        print("Feature: ", feature)
        markers = cur.fetchall()
        
        for marker in markers:
            # feature's markers
            actualfeatureinfo = {
                "type": "Feature",
                "id": marker[0],
                "properties": { 
                    "TITLE": feature[1] + " - " + marker[3],                 
                    "ADDRESS": marker[3], 
                    "TIMESTAMP": str(marker[4]), 
                    "PRECISION": marker[5],                    
                    "TOTALDETECTIONS": marker[6],                          
                    "IMAGES": [],
                    "DELTA": delta_type
                }, 
                "geometry": { 
                    "type": "Point", 
                    "coordinates": [ marker[2], marker[1]  ] 
                } 
            }		
            getmarkerimages(marker[0], feature[1], actualfeatureinfo)
            if len(actualfeatureinfo["properties"]["IMAGES"]) == 0:
                actualfeatureinfo["properties"]["IMAGES"] = [marker[7]]
            featurecontent["features"].append(actualfeatureinfo)
            n_markers += 1


        if n_markers > 0:
            featuresinfo.append(actualfeature)
            # Write JSON file
            if (delta == 'LastMonth'):
                featuremarkersfilename = unidecode.unidecode("/home/atlas/data/" + feature[1] + "_delta.geojson")
            else:
                featuremarkersfilename = unidecode.unidecode("/home/atlas/data/" + feature[1] + ".geojson")
            with io.open(featuremarkersfilename, 'w', encoding='LATIN-1') as outfile:
                str_ = json.dumps(featurecontent, cls=Encoder,
                                indent=4, sort_keys=True,
                                separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))
            print("\nFile '" + featuremarkersfilename + " created successfully!")        


'''DATABASE CONFIGURATION'''
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

# print("catalog name: " + str(catalog_id))

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, cur)

# print("encoding: " + conn.encoding)

try:
    cur.execute("SELECT id, code, title, icon FROM feature f JOIN catalog_feature cf ON f.id=cf.featureid WHERE cf.catalogid=" + str(catalog_id) + ";")
except:
    print("\nERROR: UNABLE TO GET FEATURES: ")
    exit()

features = cur.fetchall()
featuresinfo = []

# ----------- ALL -----------

query_string = 'SELECT id, latitude, longitude, address, last_timestamp, precision, total_detections, imagepath FROM marker where featureid = %s;'
getfeaturemarkers(features, "All", "", query_string)

# ----------- DELTA -----------

# search: os marcadores que foram vistos pela ultima vez há mais de 15 dias (exceptos os novos marcadores):
query_string = "SELECT id, latitude, longitude, address, last_timestamp, precision, total_detections, imagepath \
                FROM marker \
                WHERE featureid = %s \
                AND EXTRACT(YEAR FROM last_timestamp) = EXTRACT(YEAR FROM (CURRENT_DATE - INTERVAL '1 month')) \
                AND first_timestamp < CURRENT_DATE - INTERVAL '1 month' \
                AND last_timestamp < CURRENT_DATE - INTERVAL '15 days';"
getfeaturemarkers(features, "LastMonth", "removed", query_string)

# search: Novos marcadores (que foram vistos pela ultima vez nos ultimos 15 dias):
query_string = "SELECT id, latitude, longitude, address, last_timestamp, precision, total_detections, imagepath \
                FROM marker \
                WHERE featureid = %s \
                AND first_timestamp > CURRENT_DATE - INTERVAL '1 month';"
getfeaturemarkers(features, "LastMonth", "added", query_string)
    
# Write Features JSON file
featuresfilename = unidecode.unidecode("/home/atlas/data/featuresinfo.json")
with io.open(featuresfilename, 'w', encoding='LATIN-1') as outfile:
    str_ = json.dumps(featuresinfo,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
print("\nFile '" + featuresfilename + " created successfully!")