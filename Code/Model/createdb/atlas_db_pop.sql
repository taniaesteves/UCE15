INSERT INTO client (name, description) VALUES ('Miguel Bandeira', 'Vereador da C.M. Braga');

INSERT INTO catalog (title, description) VALUES ('Sinais de Trânsito', 'Sinais rodoviários da cidade de Braga');

INSERT INTO client_catalog VALUES (1, 1, 'Contracto Atlas Innovation - CMBraga');

INSERT INTO feature (title, description, icon, pathtotrainingdataset) VALUES ('Sinal Stop', 'Cedência de Passagem', 'https://openclipart.org/image/2400px/svg_to_png/33745/1269426677.png', 'trainingdataset.png');

INSERT INTO feature (title, description, icon, pathtotrainingdataset) VALUES ('Sinal Rotunda', 'Obrigação', 'https://cdn.pixabay.com/photo/2015/08/27/10/39/roundabout-910043_640.png', 'trainingdataset2.png');

INSERT INTO catalog_feature VALUES (1, 1);
INSERT INTO catalog_feature VALUES (1, 2);

INSERT INTO marker (featureid, latitude, longitude) VALUES (1, 41.560404, -8.4056225);
INSERT INTO marker (featureid, latitude, longitude) VALUES (2, 41.5581692, -8.3975698);

INSERT INTO image (markerid, imagepath) VALUES (1, 'http://i.dailymail.co.uk/i/pix/2015/02/04/2554563600000578-2939427-Apple_ditched_Google_Maps_as_the_default_navigation_app_on_iOS_d-a-44_1423052739689.jpg');
INSERT INTO image (markerid, imagepath) VALUES (1, 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/STOP_sign.jpg/220px-STOP_sign.jpg');
INSERT INTO image (markerid, imagepath) VALUES (2, 'https://street360.net/img/spain/balearic-islands/santa-ponsa_santa-ponca_balearic-islands.jpg');



SELECT title, description, icon, latitude, longitude, imagepath 
FROM ((image i JOIN marker m ON m.id=i.markerid) mi JOIN feature f ON f.id=mi.featureid) fm 
JOIN catalog_feature cf ON cf.featureid=fm.featureid 
WHERE cf.catalogid=1;