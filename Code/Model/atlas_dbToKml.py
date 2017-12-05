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
for feature in features:
    f.write(("\t\t<Style id=\"" + feature[1] + "\">\n").encode())
    f.write("\t\t\t<IconStyle>\n".encode())
    f.write("\t\t\t\t<Icon>\n".encode())
    f.write(("\t\t\t\t\t<href>" + feature[3] + "</href>\n").encode())
    f.write("\t\t\t\t</Icon>\n".encode())
    f.write("\t\t\t</IconStyle>\n".encode())
    f.write("\t\t</Style>\n".encode())

for feature in features:
    try:
        cur.execute("SELECT * FROM marker WHERE featureid=" + str(feature[0]) + ";")
    except:
        print("\nERROR: UNABLE TO GET MARKERS")
        exit()

    rows = cur.fetchall()
    markers = rows
    for marker in markers:
        f.write("\t\t<Placemark>\n".encode())
        f.write(("\t\t\t<name>" + feature[1] + "</name>\n").encode())
        f.write(("\t\t\t<styleUrl>#" + feature[1] + "</styleUrl>\n").encode())
        f.write("\t\t\t<TimeStamp><when>2012-01-02T12:01:50+01:00</when></TimeStamp>\n".encode())
        f.write("\t\t\t<description><![CDATA[".encode())
        f.write(("<img src=\"" + marker[4] + "\" height=\"200\" width=\"auto\"/>").encode())
        f.write(("]]> " + feature[1] + " </description>\n").encode())
        f.write(("\t\t\t<ExtendedData>\n").encode())
        f.write(("\t\t\t\t<Data name=\"timestamp\">\n").encode())
        f.write(("\t\t\t\t\t<value>" + str(marker[5]) + "</value>\n").encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t\t<Data name=\"precisão (%)\">\n".encode())
        f.write(("\t\t\t\t\t<value>" + str(marker[6]) + "</value>\n").encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t\t<Data name=\"nota\">\n".encode())
        f.write("\t\t\t\t\t<value></value>\n".encode())
        f.write("\t\t\t\t</Data>\n".encode())
        f.write("\t\t\t</ExtendedData>\n".encode())
        f.write("\t\t\t<Point>\n".encode())
        f.write(("\t\t\t\t<coordinates>" + str(marker[3]) + ", " + str(marker[2]) + "</coordinates>\n").encode())
        f.write("\t\t\t</Point>\n".encode())
        f.write("\t\t</Placemark>\n".encode())

f.write("\t</Document>\n".encode())
f.write("</kml>\n".encode())
f.close()

print("\nFile '" + filename + " created successfully!")
