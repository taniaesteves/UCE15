INSERT INTO client (name, description) VALUES ('Miguel Bandeira', 'Vereador da C.M. Braga');

INSERT INTO catalog (title, description) VALUES ('Sinais de Transito', 'Sinais rodoviarios da cidade de Braga');

INSERT INTO client_catalog VALUES (1, 1, 'Contracto Atlas Innovation - CMBraga');

INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('B2 - Paragem obrigatoria no cruzamento ou entroncamento', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B2.png?raw=true', 'trainingdataset.png');
INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('D4 - Rotunda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D4.png?raw=true', 'trainingdataset2.png');
INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('D1A - Sentido obrigatório', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D1A.png?raw=true', 'trainingdataset2.png');

INSERT INTO catalog_feature VALUES (1, 1);
INSERT INTO catalog_feature VALUES (1, 2);

INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (1, 41.560404, -8.4056225, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/b2_2017-11-25_20-38-25.PNG?raw=true', '2017-11-25 20:38:25', 89);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (3, 41.560404, -8.4056225, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/d4_2017-11-25_19-02-14.PNG?raw=true', '2017-11-25 20:38:54', 68);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (2, 41.5580814, -8.3976456, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/d1a_2017-11-25_20-38-54.PNG?raw=true', '2017-11-25 19:02:14', 74);


--SELECT title, description, icon, latitude, longitude, imagepath 
--FROM ((image i JOIN marker m ON m.id=i.markerid) mi JOIN feature f ON f.id=mi.featureid) fm 
--JOIN catalog_feature cf ON cf.featureid=fm.featureid 
--WHERE cf.catalogid=1;
