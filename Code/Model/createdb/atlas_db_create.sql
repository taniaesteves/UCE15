CREATE TABLE IF NOT EXISTS client (id SERIAL PRIMARY KEY, 
                                   name TEXT NOT NULL, 
                                   description TEXT);

CREATE TABLE IF NOT EXISTS catalog (id SERIAL PRIMARY KEY, 
                                    title TEXT NOT NULL, 
                                    description TEXT);

CREATE TABLE IF NOT EXISTS client_catalog (clientid INTEGER NOT NULL REFERENCES client (id), 
                                           catalogid INTEGER NOT NULL REFERENCES catalog (id), 
                                           contract TEXT NOT NULL,
                                           PRIMARY KEY (clientID, catalogID));

CREATE TABLE IF NOT EXISTS feature (id SERIAL PRIMARY KEY,
                                    code TEXT NOT NULL,
                                    title TEXT NOT NULL, 
                                    description TEXT, 
                                    icon TEXT NOT NULL,
                                    pathtotrainingdataset TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS catalog_feature (catalogid INTEGER NOT NULL REFERENCES catalog (id), 
                                            featureid INTEGER NOT NULL REFERENCES feature (id),
                                            PRIMARY KEY (catalogID, featureID));                                    

CREATE TABLE IF NOT EXISTS marker (id SERIAL PRIMARY KEY, 
                                   featureid INTEGER NOT NULL REFERENCES feature (id), 
                                   latitude DOUBLE PRECISION, 
                                   longitude DOUBLE PRECISION,
                                   imagepath TEXT NOT NULL,
                                   timestamp TIMESTAMP,
                                   precision DOUBLE PRECISION,
                                   note TEXT);
