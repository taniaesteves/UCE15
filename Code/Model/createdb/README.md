Shell 1:
	1. Inicializar a BD para o postgresql:
		> $ initdb -D atlasdb

	2. Iniciar o servidor:
		> $ postgres -D atlasdb -k.

Shell 2:
	3. Criar a DB no localhost:
		> $ createdb -h localhost

NOTAS:
	A. Para entrar na BD:
		> $ psql -h localhost
	B. Para listar as tabelas:
		> $ \d
	C. Executar queries:
		> $ querie + ';' (ex: 'SELECT * FROM client;')
	D. Executar o código através de um ficheiro ('atlas_db_create.sql'):
		> $ psql -h localhost -f atlas_db_create.sql


	Z. O ficheiro 'atlas_db_pop.sql' tem alguns inserts e uma querie só para testar o esquema da BD.