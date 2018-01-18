#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
    con = psycopg2.connect("dbname='atlas' user='atlas' host='localhost' password=''")   
except: 
    print("\nERROR: UNABLE TO CONNECT TO THE DATABASE")
    exit()

cur = con.cursor()

counter = 0

try:

	cur.execute(u"INSERT INTO client (name, description) VALUES ('Miguel Bandeira', 'Vereador da C.M. Braga');".decode("utf-8"))

	cur.execute(u"INSERT INTO catalog (title, description) VALUES ('Sinais de Transito', 'Sinais rodoviarios da cidade de Braga') RETURNING id;".decode("utf-8"))
	catalogid = cur.fetchone()[0]

	cur.execute(u"INSERT INTO client_catalog VALUES (1, 1, 'Contracto Atlas Innovation - CMBraga');".decode("utf-8"))

	# features sinais de trânsito

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A1A', 'A1A - Curva à direita', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A1A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1


	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A1B', 'A1B - Curva à esquerda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A1B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A1C', 'A1C - Curva à direita e contracurva', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A1C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A1D', 'A1D - Curva à esquerda e contracurva', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A1D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A2A', 'A2A - Lomba', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A2A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A2B', 'A2B - Depressão', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A2B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A2C', 'A2C - Lomba ou depressão', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A2C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A3A', 'A3A - Descida perigosa', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A3A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A3B', 'A3B - Subida de inclinação acentuada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A3B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A4A', 'A4A - Passagem estreita', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A4A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A4B', 'A4B - Passagem estreita', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A4B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A4C', 'A4C - Passagem estreita', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A4C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A5', 'A5 - Pavimento escorregadio', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A5.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A6', 'A6 - Projecção de gravilha', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A6.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A7A', 'A7A - Bermas baixas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A7A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A7B', 'A7B - Bermas baixas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A7B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A8', 'A8 - Saída num cais ou precipício', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A8.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A9', 'A9 - Queda de pedras', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A9.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A10', 'A10 - Ponte móvel', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A10.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A11', 'A11 - Neve ou gelo', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A11.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A12', 'A12 - Vento lateral', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A12.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A13', 'A13 - Visibilidade insuficiente', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A13.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A14', 'A14 - Crianças', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A14.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A15', 'A15 - Idosos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A15.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A16A', 'A16A - Passagem de peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A16A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A16B', 'A16B - Travessia de peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A16B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A17', 'A17 - Saída de ciclistas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A17.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A18', 'A18 - Cavaleiros', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A18.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A19A', 'A19A - Animais', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A19A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A19B', 'A19B - Animais selvagens', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A19B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A20', 'A20 - Túnel', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A20.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A21', 'A21 - Pista de aviação', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A21.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A22', 'A22 - Sinalização luminosa', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A22.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A23', 'A23 - Trabalhos na via', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A23.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A24', 'A24 - Cruzamento ou entroncamento', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A24.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A25', 'A25 - Trânsito nos dois sentidos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A25.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A26', 'A26 - Passagem de nível com guarda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A26.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A27', 'A27 - Passagem de nível sem guarda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A27.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A28', 'A28 - Intersecção com via onde circulam veículos sobre carris', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A28.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A29', 'A29 - Outros perigos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A29.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A30', 'A30 - Congestionamento', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A30.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A31', 'A31 - Obstrução da via', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A31.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A32A', 'A32A - Local de passagem de nível sem guarda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A32A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('A32B', 'A32B - Local de passagem de nível sem guarda com duas ou mais vias', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/A32B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B1', 'B1 - Cedência de passagem', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B1.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B2', 'B2 - Paragem obrigatória no cruzamento ou entroncamento', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B2.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B3', 'B3 - Via com prioridade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B3.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B4', 'B4 - Fim de via com prioridade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B4.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B5', 'B5 - Cedência de passagem nos estreitamentos da faixa de rodagem', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B5.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B6', 'B6 - Prioridade nos estreitamentos da faixa de rodagem', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B6.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B7', 'B7 - Aproximação de rotunda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B7.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B8', 'B8 - Cruzamento com via sem prioridade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B8.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B9A', 'B9A - Entroncamento com via sem prioridade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B9A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B9B', 'B9B - Entroncamento com via sem prioridade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B9B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B9C', 'B9C - Entroncamento com via sem prioridade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B9C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('B9D', 'B9D - Entroncamento com via sem prioridade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B9D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C1', 'C1 - Sentido proibido', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C1.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C2', 'C2 - Trânsito proibido', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C2.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3A', 'C3A - Trânsito proibido a automóveis e motociclos com carro', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3B', 'C3B - Trânsito proibido a automóveis pesados', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3C', 'C3C - Trânsito proibido a automóveis de mercadorias', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3D', 'C3D - Trânsito proibido a automóveis de mercadorias de peso total superior a ...t', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3E', 'C3E - Trânsito proibido a motociclos simples', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3E.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3F', 'C3F - Trânsito proibido a ciclomotores', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3F.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3G', 'C3G - Trânsito proibido a velocípedes', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3G.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3H', 'C3H - Trânsito proibido a veículos agrícolas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3H.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3I', 'C3I - Trânsito proibido a veículos de tracção animal', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3I.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3J', 'C3J - Trânsito proibido a carros de mão', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3J.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3L', 'C3L - Trânsito proibido a peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3L.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3M', 'C3M - Trânsito proibido a cavaleiros', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3M.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3N', 'C3N - Trânsito proibido a veículos com reboque', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3N.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3O', 'C3O - Trânsito proibido a veículos com reboque de dois ou mais eixos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3O.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3P', 'C3P - Trânsito proibido a veículos transportando mercadorias perigosas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3P.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3Q', 'C3Q - Trânsito proibido a veículos transportando produtos facilmente inflamáveis ou explosivos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3Q.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C3R', 'C3R - Trânsito proibido a veículos transportando produtos susceptíveis de poluírem as águas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C3R.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C4A', 'C4A - Trânsito proibido a automóveis e motociclos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C4A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C4B', 'C4B - Trânsito proibido a automóveis de mercadorias e a veículos a motor com reboque', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C4B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C4C', 'C4C - Trânsito proibido a automóveis, a motociclos e a veículos de tracção animal', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C4C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C4D', 'C4D - Trânsito proibido a automóveis de mercadorias e a veículos de tracção animal', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C4D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C4E', 'C4E - Trânsito proibido a peões, a animais e a veículos que não sejam automóveis ou motociclos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C4E.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C4F', 'C4F - Trânsito proibido a veículos de duas rodas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C4F.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C5', 'C5 - Trânsito proibido a veículos de peso por eixo superior a ...t', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C5.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C6', 'C6 - Trânsito proibido a veículos de peso total superior a ...t', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C6.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C7', 'C7 - Trânsito proibido a veículos ou conjunto de veículos de comprimento superior a ...m', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C7.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C8', 'C8 - Trânsito proibido a veículos de largura superior a ...m', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C8.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C9', 'C9 - Trânsito proibido a veículos de altura superior a ...m', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C9.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C10', 'C10 - Proibição de transitar a menos de ...m do veículo precedente', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C10.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C11A', 'C11A - Proibição de virar à direita', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C11A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C11B', 'C11B - Proibição de virar à esquerda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C11B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C12', 'C12 - Proibição de inversão do sentido de marcha', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C12.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C13', 'C13 - Proibição de exceder a velocidade máxima de ...Km/h', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C13.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C14A', 'C14A - Proibição de ultrapassar', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C14A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C14B', 'C14B - Proibição de ultrapassar para automóveis pesados', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C14B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C14C', 'C14C - Proibição de ultrapassar para motociclos e ciclomotores', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C14C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C15', 'C15 - Estacionamento proibido', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C15.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C16', 'C16 - Paragem e estacionamento proibidos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C16.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C17', 'C17 - Proibição de sinais sonoros', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C17.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C18', 'C18 - Paragem obrigatória na alfândega', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C18.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C19', 'C19 - Outras paragens obrigatórias', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C19.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C20A', 'C20A - Fim de todas as proibições impostas anteriormente por sinalização a veículos em marcha', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C20A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C20B', 'C20B - Fim da limitação de velocidade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C20B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C20C', 'C20C - Fim da proibição de ultrapassar', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C20C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C20D', 'C20D - Fim da proibição de ultrapassar para automóveis pesados', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C20D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C20E', 'C20E - Fim da proibição de ultrapassar para motociclos e ciclomotores', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C20E.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C21', 'C21 - Fim de paragem ou estacionamento proibidos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C21.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('C22', 'C22 - Fim da proibição de sinais sonoros', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/C22.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D1A', 'D1A - Sentido obrigatório', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D1A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D1B', 'D1B - Sentido obrigatório', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D1B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D1C', 'D1C - Sentido obrigatório', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D1C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D1D', 'D1D - Sentido obrigatório', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D1D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D1E', 'D1E - Sentido obrigatório', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D1E.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D2A', 'D2A - Sentidos obrigatórios possíveis', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D2A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D2B', 'D2B - Sentidos obrigatórios possíveis', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D2B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D2C', 'D2C - Sentidos obrigatórios possíveis', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D2C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D3A', 'D3A - Obrigação de contornar a placa ou obstáculo', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D3A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D3B', 'D3B - Obrigação de contornar a placa ou obstáculo', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D3B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D4', 'D4 - Rotunda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D4.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D5A', 'D5A - Via obrigatória para automóveis de mercadorias', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D5A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D5B', 'D5B - Via obrigatória para automóveis pesados', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D5B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D6', 'D6 - Via reservada a veículos de transporte público', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D6.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D7A', 'D7A - Pista obrigatória para velocípedes', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D7A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D7B', 'D7B - Pista obrigatória para peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D7B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D7C', 'D7C - Pista obrigatória para cavaleiros', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D7C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D7D', 'D7D - Pista obrigatória para gado e manada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D7D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D7E', 'D7E - Pista obrigatória para peões e velocípedes', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D7E.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D7F', 'D7F - Pista obrigatória para peões e velocípedes', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D7F.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D8', 'D8 - Obrigação de transitar à velocidade mínima de … km/h', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D8.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D9', 'D9 - Obrigação de utilizar correntes de neve', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D9.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D10', 'D10 - Obrigação de utilizar as luzes de cruzamento (médios) acesas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D10.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D11A', 'D11A - Fim da via obrigatória para automóveis de mercadorias', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D11A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D11B', 'D11B - Fim da via obrigatória para automóveis pesados', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D11B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D12', 'D12 - Fim da via reservada a veículos de transporte público', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D12.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D13A', 'D13A - Fim da pista obrigatória para velocípedes', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D13A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D13B', 'D13B - Fim da pista obrigatória para peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D13B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D13C', 'D13C - Fim da pista obrigatória para cavaleiros', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D13C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D13D', 'D13D - Fim da pista obrigatória para gado em manada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D13D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D13E', 'D13E - Fim da pista obrigatória para peões e velocípedes', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D13E.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D13F', 'D13F - Fim da pista obrigatória para peões e velocípedes', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D13F.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D14', 'D14 - Fim da obrigação de transitar à velocidade mínima de … km/h', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D14.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D15', 'D15 - Fim da obrigação de utilizar correntes de neve', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D15.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('D16', 'D16 - Fim da obrigação de utilizar as luzes de cruzamento acesas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D16.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('E1', 'E1 - Destinos sobre o itinerário', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/E1.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('E2', 'E2 - Destinos de saída', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/E2.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('E3', 'E3 - Sinal de selecção lateral', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/E3.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('F1A', 'F1A - Aplicação de prescrição a via de trânsito', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/F1A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('F1B', 'F1B - Aplicação de prescrição a via de trânsito', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/F1B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('F1C', 'F1C - Aplicação de prescrição a via de trânsito', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/F1C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('F2', 'F2 - Via de trânsito reservada a veículos de transporte público', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/F2.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G1', 'G1 - Zona de estacionamento autorizado', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G1.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G2A', 'G2A - Zona de estacionamento proibido', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G2A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G2B', 'G2B - Zona de estacionamento proibido', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G2B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G3', 'G3 - Zona de paragem e estacionamento proibidos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G3.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G4', 'G4 - Zona de velocidade limitada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G4.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G5A', 'G5A - Zona de trânsito proibido', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G5A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G5B', 'G5B - Zona de trânsito proibido', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G5B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G6', 'G6 - Fim de zona de estacionamento autorizado', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G6.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G7A', 'G7A - Fim de zona de paragem e estacionamento proibidos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G7A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G7B', 'G7B - Fim de zona de paragem e estacionamento proibidos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G7B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G8', 'G8 - Fim de zona de velocidade limitada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G8.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('G9', 'G9 - Fim de todas as proibições impostas na zona', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/G9.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H1A', 'H1A - Estacionamento autorizado', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H1A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H1B', 'H1B - Estacionamento autorizado', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H1B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H2', 'H2 - Hospital', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H2.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H3', 'H3 - Trânsito de sentido único', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H3.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H4', 'H4 - Via pública sem saída', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H4.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H5', 'H5 - Correntes de neve recomendadas', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H5.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H6', 'H6 - Velocidade recomendada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H6.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H7', 'H7 - Passagem para peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H7.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H8A', 'H8A - Passagem desnivelada para peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H8A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H8B', 'H8B - Passagem desnivelada para peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H8B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H9', 'H9 - Hospital com urgência médica', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H9.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H10', 'H10 - Posto de socorros', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H10.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H11', 'H11 - Oficina', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H11.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H12', 'H12 - Telefone', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H12.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H13A', 'H13A - Posto de abastecimento de combustível', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H13A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H13B', 'H13B - Posto de abastecimento de combustível com GPL', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H13B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H13C', 'H13C - Posto de abastecimento de combustível com serviço a veículos eléctricos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H13C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H13D', 'H13D - Posto de abastecimento de combustível com GPL e com serviço a veículos eléctricos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H13D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H14A', 'H14A - Parque de campismo', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H14A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H14B', 'H14B - Parque para reboques de campismo', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H14B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H14C', 'H14C - Parque misto para campismo e reboques de campismo', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H14C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H15', 'H15 - Telefone de emergência', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H15.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H16A', 'H16A - Pousada ou estalagem', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H16A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H16B', 'H16B - Albergue', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H16B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H16C', 'H16C - Pousada de juventude', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H16C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H16D', 'H16D - Turismo rural', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H16D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H17', 'H17 - Hotel', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H17.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H18', 'H18 - Restaurante', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H18.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H19', 'H19 - Café ou bar', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H19.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H20A', 'H20A - Paragem de veículos de transporte colectivo de passageiros', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H20A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H20B', 'H20B - Paragem de veículos de transporte colectivo de passageiros que transitem sobre carris', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H20B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H20C', 'H20C - Paragem de veículos afectos ao transporte de crianças', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H20C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H21', 'H21 - Aeroporto', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H21.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H22', 'H22 - Posto de informações', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H22.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H23', 'H23 - Estação de radiodifusão', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H23.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H24', 'H24 - Auto-estrada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H24.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H25', 'H25 - Via reservada a automóveis e motociclos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H25.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H26', 'H26 - Escapatória', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H26.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H27', 'H27 - Inversão do sentido de marcha', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H27.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H28', 'H28 - Limites de velocidade', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H28.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H29A', 'H29A - Identificação de país', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H29A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H29B', 'H29B - Identificação de país', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H29B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H30', 'H30 - Praticabilidade da via', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H30.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H31A', 'H31A - Número e sentido das vias de trânsito', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H31A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H31B', 'H31B - Número e sentido das vias de trânsito', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H31B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H31C', 'H31C - Número e sentido das vias de trânsito', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H31C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H31D', 'H31D - Número e sentido das vias de trânsito', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H31D.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H32', 'H32 - Supressão de via de trânsito', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H32.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H33', 'H33 - Via verde', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H33.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H34', 'H34 - Centro de inspecções', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H34.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H35', 'H35 - Túnel', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H35.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H36', 'H36 - Fim da recomendação do uso de correntes de neve', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H36.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H37', 'H37 - Fim da velocidade recomendada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H37.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H38', 'H38 - Fim de auto-estrada', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H38.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H39', 'H39 - Fim de via reservada a automóveis e motociclos', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H39.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H40', 'H40 - Fim de estacionamento autorizado', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H40.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H41', 'H41 - Fim de túnel', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H41.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H42', 'H42 - Velocidade média', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H42.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H43', 'H43 - Velocidade instantânea', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H43.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H44A', 'H44A - Lanço com cobrança electrónica de portagem', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H44A.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H44B', 'H44B - Lanço com cobrança electrónica de portagem', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H44B.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H44C', 'H44C - Lanço com cobrança electrónica de portagem', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H44C.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1

	cur.execute(u"INSERT INTO feature (code, title, icon, pathtotrainingdataset) VALUES ('H45', 'H45 - Fim de lanço com cobrança electrónica de portagem', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H45.png?raw=true', 'trainingdataset.tfrecord') RETURNING id;".decode("utf-8"))
	id_of_new_row = cur.fetchone()[0]
	cur.execute("INSERT INTO catalog_feature VALUES (" + str(catalogid) + " , " + str(id_of_new_row) + ")")
	counter = counter + 1


	con.commit()
    

except psycopg2.DatabaseError as e:
    print("\nERROR: UNABLE TO INSERT features")
    print("Error: %s" + e)
    exit()

print("\n " + counter + " FEATURES INSERTED")
