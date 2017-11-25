INSERT INTO client (name, description) VALUES ('Miguel Bandeira', 'Vereador da C.M. Braga');

INSERT INTO catalog (title, description) VALUES ('Sinais de Trânsito', 'Sinais rodoviários da cidade de Braga');

INSERT INTO client_catalog VALUES (1, 1, 'Contracto Atlas Innovation - CMBraga');

INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('Sinal Stop', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/B2.png?raw=true', 'trainingdataset.png');

INSERT INTO feature (title, icon, pathtotrainingdataset) VALUES ('D4 - Rotunda', 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/icons/D4.png?raw=true', 'trainingdataset2.png');

INSERT INTO catalog_feature VALUES (1, 1);
INSERT INTO catalog_feature VALUES (1, 2);

INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (1, 41.560404, -8.4056225, 'http://i.dailymail.co.uk/i/pix/2015/02/04/2554563600000578-2939427-Apple_ditched_Google_Maps_as_the_default_navigation_app_on_iOS_d-a-44_1423052739689.jpg', '2017-11-25 20:38:25', 89);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (3, 41.560404, -8.4056225, 'http://i.dailymail.co.uk/i/pix/2015/02/04/2554563600000578-2939427-Apple_ditched_Google_Maps_as_the_default_navigation_app_on_iOS_d-a-44_1423052739689.jpg', '2017-11-25 20:38:54', 68);
INSERT INTO marker (featureid, latitude, longitude, imagepath, timestamp, precision) VALUES (2, 41.5580814, -8.3976456, 'https://street360.net/img/spain/balearic-islands/santa-ponsa_santa-ponca_balearic-islands.jpg', '2017-11-25 19:02:14', 74);


--SELECT title, description, icon, latitude, longitude, imagepath 
--FROM ((image i JOIN marker m ON m.id=i.markerid) mi JOIN feature f ON f.id=mi.featureid) fm 
--JOIN catalog_feature cf ON cf.featureid=fm.featureid 
--WHERE cf.catalogid=1;