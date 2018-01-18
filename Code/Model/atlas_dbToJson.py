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

# JSON FILE
filename = unidecode.unidecode(catalog_title.replace(" ", "_") + ".json").lower()
f = open(filename, "w")


catalog_id = rows[0][0]

f.write("{\n")


try:
    cur.execute("SELECT m.id, f.title, m.latitude, m.longitude, m.imagepath, m.timestamp, m.precision FROM marker m \
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
    f.write("\t\t\"timestamp\" : \""+str(marker[5])+ "\",\n")
    f.write("\t\t\"precision\" : \""+str(marker[6])+ "\"\n")
    f.write("\t},\n")

f.write("}")
f.close()

print("\nFile '" + filename + " created successfully!")
