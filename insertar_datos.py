import json
import psycopg2

DBCONFIG = {
    "host": "localhost",
    "database": "proyectowifidb",
    "user": "piuser",
    "password": "tu_contraseña"
}

def conectar_postgres():
    try:
        conexion = psycopg2.connect(**DB_CONFIG)
        conexion.autocommit = True
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def insertar_datos(cursor, archivo_json):
    try:
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
        for dispositivo in datos["dispositivos"]:
            cursor.execute("""
                INSERT INTO dispositivos (mac, ip, nombre)
                VALUES (%s, %s, %s)
                ON CONFLICT (mac) DO NOTHING
            """, (dispositivo["mac"], dispositivo["ip"], dispositivo["nombre"]))
            print(f"Dispositivo '{dispositivo['nombre']}' registrado.")
    except Exception as e:
        print(f"Error al insertar datos: {e}")

def main():
    conexion = conectar_postgres()
    if conexion:
        try:
            cursor = conexion.cursor()
            insertar_datos(cursor, 'datos.json')
        finally:
            cursor.close()
            conexion.close()

if __name == "__main":
    main()
