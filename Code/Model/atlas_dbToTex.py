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
filename = "/home/atlas/data/" + unidecode.unidecode(catalog_title.replace(" ", "_") + ".tex").lower()
f = io.open(filename, "w", encoding='utf-8')

f.write("\\documentclass[a4paper,]{report}\n")
f.write("\\usepackage[utf8]{inputenc}\n")
f.write("\\usepackage{natbib}\n")
f.write("\\usepackage{graphicx}\n\n")
f.write("\\usepackage{pdfpages}\n")
f.write("\\usepackage{float}\n")
f.write("\\usepackage{grffile}\n")

f.write("\\begin{document}\n")
f.write("\\includepdf{Capa.pdf}\n")


f.write("\n")

catalog_id = rows[0][0]

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, cur)
print("encoding: " + conn.encoding)

try:
    cur.execute("SELECT m.id, f.title, m.latitude, m.longitude, m.imagepath, m.first_timestamp, m.last_timestamp, m.precision, m.total_detections, m.address FROM marker m \
                 inner join feature f ON m.featureid= f.id \
                 inner join catalog_feature cf ON cf.featureid=f.id where cf.catalogid =" + str(catalog_id) + ";")
except:
    print("\nERROR: UNABLE TO GET FEATURES")
    exit()

f.write("\chapter{ Markers }\n")

rows = cur.fetchall()
markers = rows
incre = 1
for marker in markers:
    f.write("\section{marker "+str(incre) +"}\n")
    f.write("\\begin{itemize}\n")
    f.write("\item feature: " + marker[1] + "\n" )
    f.write("\item latitude: "+ str(marker[2])+ "\n")
    f.write("\item longitude: "+ str(marker[3])+ "\n")
    f.write("\item first timestamp: "+ str(marker[5])+ "\n")
    f.write("\item last timestamp: "+ str(marker[6])+ "\n")
    f.write("\item precision: "+ str(marker[7])+ "\n")
    f.write("\item total detections: "+ str(marker[8])+ "\n")
    f.write("\item Address: "+ str(marker[9])+ "\n")
    f.write("\\begin{figure}[H]\n")
    f.write("\t\\centering\n")
    f.write("\t\\includegraphics[width=0.5\\textwidth]{Catalogs/"+ str(marker[4]) +"}\n")
    f.write("\\end{figure}\n")
    incre += 1
    f.write("\\end{itemize}\n")

f.write("\end{document} \n")
f.close()

print("\nFile '" + filename + " created successfully!")
