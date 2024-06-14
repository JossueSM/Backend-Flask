import psycopg2

def conectar_database():
    # Establecer la conexión a la base de datos
    conn = psycopg2.connect(
        dbname='flask',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )
    return conn
