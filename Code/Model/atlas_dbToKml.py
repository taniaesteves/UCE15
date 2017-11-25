import psycopg2
import unidecode
from pprint import pprint

# DATABASE CONFIGURATION

dbname   = 'atlasdb'
user     = 'tania'
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
f = open(filename, "w")
f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
f.write("<kml xmlns=\"http://earth.google.com/kml/2.2\">\n")
f.write("\t<Document>\n")

f.write("\t\t<name>" + catalog_title + "</name>\n")

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
    f.write("\t\t<Style id=\"" + feature[1] + "\">\n")
    f.write("\t\t\t<IconStyle>\n")
    f.write("\t\t\t\t<Icon>\n")
    f.write("\t\t\t\t\t<href>" + feature[3] + "</href>\n")
    f.write("\t\t\t\t</Icon>\n")
    f.write("\t\t\t</IconStyle>\n")
    f.write("\t\t</Style>\n")

for feature in features:
    try:
        cur.execute("SELECT * FROM marker WHERE featureid=" + str(feature[0]) + ";")
    except:
        print("\nERROR: UNABLE TO GET MARKERS")
        exit()

    rows = cur.fetchall()
    markers = rows
    for marker in markers:
        f.write("\t\t<Placemark>\n")
        f.write("\t\t\t<name>" + feature[1] + "</name>\n")
        f.write("\t\t\t<styleUrl>#" + feature[1] + "</styleUrl>\n")
        f.write("\t\t\t<description><![CDATA[")
        f.write("<img src=\"" + marker[4] + "\" height=\"200\" width=\"auto\"/>")
        f.write("]]></description>\n")
        f.write("\t\t\t<Point>\n")
        f.write("\t\t\t\t<coordinates>" + str(marker[3]) + ", " + str(marker[2]) + "</coordinates>\n")
        f.write("\t\t\t</Point>\n")
        f.write("\t\t</Placemark>\n")

f.write("\t</Document>\n")
f.write("</kml>\n")
f.close()

print("\nFile '" + filename + " created successfully!")
