import psycopg2

parametros = { "host": "localhost", "database": "python-bd", "user": "postgres", "password": "psql"}

conexao = None

conexao = psycopg2.connect(**parametros)

if conexao is not None:
    print("Conexao realizada com sucesso!")
else:
    print("Erro ao conectar com o banco de dados!!")
