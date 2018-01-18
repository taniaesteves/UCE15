#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect("dbname='atlas' user='atlas' host='localhost' password=''")   
    
    cur = con.cursor()

    cur.execute("INSERT INTO client (name, description) VALUES ('Miguel Bandeira', 'Vereador da C.M. Braga');")
    cur.execute("INSERT INTO catalog (title, description) VALUES ('Sinais de Transito', 'Sinais rodoviarios da cidade de Braga');")
    cur.execute("INSERT INTO client_catalog VALUES (1, 1, 'Contracto Atlas Innovation - CMBraga');")

    cur.execute("INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B2','B2 - Paragem obrigatoria no cruzamento ou entroncamento', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B2.png?raw=true', 'trainingdataset.png');")

    cur.execute("INSERT INTO catalog_feature VALUES (1, 1);")
    
    con.commit()
    

except psycopg2.DatabaseError as e:
    
    if con:
        con.rollback()
    
    print ('Error %s' % e)
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

