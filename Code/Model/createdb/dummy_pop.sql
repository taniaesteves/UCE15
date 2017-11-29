INSERT INTO client (name, description) VALUES ('Miguel Bandeira', 'Vereador da C.M. Braga');

INSERT INTO catalog (title, description) VALUES ('Sinais de Trânsito', 'Sinais rodoviários da cidade de Braga');

INSERT INTO client_catalog VALUES (1, 1, 'Contracto Atlas Innovation - CMBraga');

INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('B2 - Paragem obrigatória no cruzamento ou entroncamento', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B2.png?raw=true', 'trainingdataset.png');
INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('D4 - Rotunda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D4.png?raw=true', 'trainingdataset2.png');
INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('D1A - Sentido obrigatório', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D1A.png?raw=true', 'trainingdataset2.png');
INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('D1C - Sentido obrigatório', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D1C.png?raw=true', 'trainingdataset2.png');
INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('H7 - Passagem para peões', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/H7.png?raw=true', 'trainingdataset2.png');


INSERT INTO catalog_feature VALUES (1, 1);
INSERT INTO catalog_feature VALUES (1, 2);
INSERT INTO catalog_feature VALUES (1, 3);
INSERT INTO catalog_feature VALUES (1, 4);
INSERT INTO catalog_feature VALUES (1, 5); 

INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (1, 41.560404, -8.4056225, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/b2_2017-11-25_20-38-25.PNG?raw=true', '2017-11-25 20:38:25', 89);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (2, 41.560404, -8.4056225, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/d4_2017-11-25_19-02-14.PNG?raw=true', '2017-11-25 19:02:14', 68);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (3, 41.5580814, -8.3976456, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/d1a_2017-11-25_20-38-54.PNG?raw=true', '2017-11-25 20:38:54', 74);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (4, 41.1463503, -8.3976456, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/d1c_2017-11-25_18-38-54.PNG?raw=true', '2017-11-25 18:38:54', 79);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (5, 41.5580039, -8.3983606, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/h7_2017-11-25_17-38-52.PNG?raw=true', '2017-11-25 17:38:52', 82);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (2, 41.5580606, -8.3981922, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/d4_2017-11-25_17-15-52.PNG?raw=true', '2017-11-25 17:15:52', 80);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (5, 41.5580278, -8.3979252, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/h7_2017-11-25_12-25-52.PNG?raw=true', '2017-11-25 12:25:52', 77);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (5, 41.5570358, -8.3977584, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/h7_2017-11-25_14-25-52.PNG?raw=true', '2017-11-25 14:25:52', 79);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (5, 41.5570358, -8.3977584, 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/h7_2017-11-25_14-25-54.PNG?raw=true', '2017-11-25 14:25:54', 79);