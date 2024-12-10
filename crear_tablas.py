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

def crear_tablas(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dispositivos (
                id SERIAL PRIMARY KEY,
                mac VARCHAR(17) NOT NULL UNIQUE,
                ip VARCHAR(15) NOT NULL,
                nombre VARCHAR(100),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS paquetes (
                id SERIAL PRIMARY KEY,
                protocolo VARCHAR(10) NOT NULL,
                origen VARCHAR(15) NOT NULL,
                destino VARCHAR(15) NOT NULL,
                tamaño INTEGER NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                dispositivo_id INTEGER REFERENCES dispositivos(id) ON DELETE CASCADE
            )
        """)
        print("Tablas creadas correctamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")

def main():
    conexion = conectar_postgres()
    if conexion:
        try:
            cursor = conexion.cursor()
            crear_tablas(cursor)
        finally:
            cursor.close()
            conexion.close()

if __name == "__main":
    main()
