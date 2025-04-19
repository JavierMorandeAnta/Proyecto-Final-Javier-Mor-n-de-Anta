#Esto realiza una prueba de conexión a una base de datos PostgreSQL utilizando psycopg2.

import psycopg2

try:
    connection = psycopg2.connect(
        dbname="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
finally:
    if 'connection' in locals() and connection:
        connection.close()