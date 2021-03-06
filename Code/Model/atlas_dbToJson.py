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
filename = "/home/atlas/data/" + unidecode.unidecode(catalog_title.replace(" ", "_") + ".json").lower()
f = io.open(filename, "w", encoding='utf-8')

catalog_id = rows[0][0]

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, cur)
print("encoding: " + conn.encoding)

f.write("{\n")

try:
    cur.execute("SELECT m.id, f.title, m.latitude, m.longitude, m.imagepath, m.first_timestamp, m.last_timestamp, m.precision, m.total_detections, m.address FROM marker m \
                 inner join feature f ON m.featureid= f.id \
                 inner join catalog_feature cf ON cf.featureid=f.id where cf.catalogid =" + str(catalog_id) + ";")
except:
    print("\nERROR: UNABLE TO GET FEATURES")
    exit()

rows = cur.fetchall()
markers = rows
for marker in markers:
    f.write("\t\"marker" + str(marker[0]) +"\" : {\n")
    f.write("\t\t\"feature\" : \""+marker[1]+ "\",\n")
    f.write("\t\t\"latitude\" : "+str(marker[2])+ ",\n")
    f.write("\t\t\"longitude\" : "+str(marker[3])+ ",\n")
    f.write("\t\t\"imgURL\" : \""+marker[4]+ "\",\n")
    f.write("\t\t\"first timestamp\" : \""+ str(marker[5])+ "\",\n")
    f.write("\t\t\"last timestamp\" : \""+ str(marker[6])+ "\",\n")
    f.write("\t\t\"precision\" : \""+str(marker[7])+ "\",\n")
    f.write("\t\t\"total detections\" : \"" + str(marker[8])+ "\",\n")
    f.write("\t\t\"Address\" : \"" + str(marker[9])+ "\"\n")
    f.write("\t},\n")

f.write("}")
f.close()

print("\nFile '" + filename + " created successfully!")