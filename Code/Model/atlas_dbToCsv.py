#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import unidecode
import psycopg2.extensions
import unidecode
import io

from pprint import pprint

# DATABASE CONFIGURATION

try:
    to_unicode = unicode
except:
    to_unicode = str


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

conn.set_client_encoding('utf-8')
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


# Tex FILE
filename = "/home/atlas/data/" + unidecode.unidecode(catalog_title.replace(" ", "_") + ".csv").lower()
f = io.open(filename, "w", encoding='utf-16')

catalog_id = rows[0][0]

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, cur)
print("encoding: " + conn.encoding)


try:
    cur.execute("SELECT m.id, f.title, m.latitude, m.longitude, m.first_timestamp, m.last_timestamp, m.precision, m.total_detections, m.address FROM marker m \
                 inner join feature f ON m.featureid= f.id \
                 inner join catalog_feature cf ON cf.featureid=f.id where cf.catalogid =" + str(catalog_id) + ";")
except:
    print("\nERROR: UNABLE TO GET FEATURES")
    exit()


f.write("sep=,\nId Marker,Feauture,Latitude,Longitude,First Timestamp,Last Timestamp,Precision,Total detections,Address\n")


rows = cur.fetchall()
markers = rows
for marker in markers:
    f.write("\"" +str(marker[0])+ "\",")
    f.write("\"" +str(marker[1])+ "\",")
    f.write("\"" +str(marker[2])+ "\",")
    f.write("\"" +str(marker[3])+ "\",")
    f.write("\"" +str(marker[4])+ "\",")
    f.write("\"" +str(marker[5])+ "\",")
    f.write("\"" +str(marker[6])+ "\",")
    f.write("\"" +str(marker[7])+ "\",")
    f.write("\"" + str(marker[8])+ "\"\n")

f.close()

print("\nFile '" + filename + " created successfully!")