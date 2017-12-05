#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
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

# KML FILE HEAD
filename = unidecode.unidecode(catalog_title.replace(" ", "_") + ".kml").lower()
f = open(filename, "wb")
f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n".encode())
f.write("<kml xmlns=\"http://earth.google.com/kml/2.2\">\n".encode())
f.write("\t<Document>\n".encode())

f.write(("\t\t<name>" + catalog_title + "</name>\n").encode())

catalog_id = rows[0][0]

try:
    cur.execute("SELECT id, title, description, icon FROM feature f JOIN catalog_feature cf ON f.id=cf.featureid \
                 WHERE cf.catalogid=" + str(catalog_id) + ";")
except:
    print("\nERROR: UNABLE TO GET FEATURES")
    exit()

rows = cur.fetchall()
features = rows

f.write(("\t\t<Style id=\"multiplemarkes\">\n").encode())
f.write("\t\t\t<IconStyle>\n".encode())
f.write("\t\t\t\t<Icon>\n".encode())
f.write(("\t\t\t\t\t<href>https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/multiplemarkers.png?raw=true</href>\n").encode())
f.write("\t\t\t\t</Icon>\n".encode())
f.write("\t\t\t</IconStyle>\n".encode())
f.write("\t\t</Style>\n".encode())

for feature in features:
    f.write(("\t\t<Style id=\"" + feature[1] + "\">\n").encode())
    f.write("\t\t\t<IconStyle>\n".encode())
    f.write("\t\t\t\t<Icon>\n".encode())
    f.write(("\t\t\t\t\t<href>" + feature[3] + "</href>\n").encode())
    f.write("\t\t\t\t</Icon>\n".encode())
    f.write("\t\t\t</IconStyle>\n".encode())
    f.write("\t\t</Style>\n".encode())
try:
    cur.execute("SELECT title as featuretitle, latitude, longitude, imagepath, timestamp, precision, note \
                 FROM marker m JOIN feature f ON m.featureid=f.id \
                 ORDER BY latitude, longitude;")
except:
    print("\nERROR: UNABLE TO GET MARKERS")
    exit()

rows = cur.fetchall()
marker_dict = {} 
for row in rows:
    key = str(row[1]) + "," + str(row[2])
    newmarker = { "featuretitle": row[0],
                  "imagepath": row[3],
                  "timestamp": row[4],
                  "precision": row[5],
                  "note": row[6] }

    if key in marker_dict:
        marker_dict[key].append(newmarker)
    else:
        marker_dict[key] = [newmarker]
        
for key in marker_dict.keys():
    lat, lon = key.split(',')
    markers = marker_dict[key]
    f.write("\t\t<Placemark>\n".encode())

    if len(marker_dict[key]) > 1:
        f.write(("\t\t\t<name>Multiple markers</name>\n").encode())
        f.write(("\t\t\t<styleUrl>#multiplemarkes</styleUrl>\n").encode())
        f.write("\t\t\t<description><![CDATA[".encode())
        for marker in markers:
            f.write(("<img src=\"" + marker["imagepath"] + "\" height=\"200\" width=\"auto\"/>").encode())
        f.write(("]]> " + markers[0]["featuretitle"] + " </description>\n").encode())
        f.write(("\t\t\t<ExtendedData>\n").encode())
        f.write(("\t\t\t\t<Data name=\"timestamp\">\n").encode())
        f.write(("\t\t\t\t\t<value>" + str(markers[0]["timestamp"]) + "</value>\n").encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t\t<Data name=\"precisão (%)\">\n".encode())
        f.write(("\t\t\t\t\t<value>" + str(markers[0]["precision"]) + "</value>\n").encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t\t<Data name=\"nota\">\n".encode())
        f.write(("\t\t\t\t\t<value>" + str(markers[0]["note"]) + "</value>\n").encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t</ExtendedData>\n".encode())
    else:
        f.write(("\t\t\t<name>" + markers[0]["featuretitle"] + "</name>\n").encode())
        f.write(("\t\t\t<styleUrl>#" + markers[0]["featuretitle"] + "</styleUrl>\n").encode())
        f.write("\t\t\t<description><![CDATA[".encode())
        f.write(("<img src=\"" + markers[0]["imagepath"] + "\" height=\"200\" width=\"auto\"/>").encode())
        f.write(("]]> " + markers[0]["featuretitle"] + " </description>\n").encode())
        f.write(("\t\t\t<ExtendedData>\n").encode())
        f.write(("\t\t\t\t<Data name=\"timestamp\">\n").encode())
        f.write(("\t\t\t\t\t<value>" + str(markers[0]["timestamp"]) + "</value>\n").encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t\t<Data name=\"precisão (%)\">\n".encode())
        f.write(("\t\t\t\t\t<value>" + str(markers[0]["precision"]) + "</value>\n").encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t\t<Data name=\"nota\">\n".encode())
        f.write(("\t\t\t\t\t<value>" + str(markers[0]["note"]) + "</value>\n").encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t</ExtendedData>\n".encode())
    
    f.write("\t\t\t<Point>\n".encode())
    f.write(("\t\t\t\t<coordinates>" + lon + ", " + lat + "</coordinates>\n").encode())
    f.write("\t\t\t</Point>\n".encode())
    f.write("\t\t</Placemark>\n".encode())

f.write("\t</Document>\n".encode())
f.write("</kml>\n".encode())
f.close()

print("\nFile '" + filename + " created successfully!")
