INSERT INTO client (name, description) VALUES ('Miguel Bandeira', 'Vereador da C.M. Braga');

INSERT INTO catalog (title, description) VALUES ('Sinais de Trânsito', 'Sinais rodoviários da cidade de Braga');

INSERT INTO client_catalog VALUES (1, 1, 'Contracto Atlas Innovation - CMBraga');

INSERT INTO feature (title, description, icon, pathtotrainingdataset) VALUES ('Sinal Stop', 'Cedência de Passagem', 'stop.png', 'trainingdataset.png');

INSERT INTO feature (title, description, icon, pathtotrainingdataset) VALUES ('Sinal Rotunda', 'Obrigação', 'roundabout.png', 'trainingdataset2.png');

INSERT INTO catalog_feature VALUES (1, 1);

INSERT INTO marker (featureid, latitude, longitude) VALUES (1, 41.560404, -8.4056225);
INSERT INTO marker (featureid, latitude, longitude) VALUES (2, 41.5581692, -8.3975698);

INSERT INTO image (markerid, imagepath) VALUES (1, 'marker1image1.png');
INSERT INTO image (markerid, imagepath) VALUES (1, 'marker1image2.png');
INSERT INTO image (markerid, imagepath) VALUES (2, 'marker2image1.png');




SELECT title, description, icon, latitude, longitude, imagepath 
FROM ((image i JOIN marker m ON m.id=i.markerid) mi JOIN feature f ON f.id=mi.featureid) fm 
JOIN catalog_feature cf ON cf.featureid=fm.featureid 
WHERE cf.catalogid=1;