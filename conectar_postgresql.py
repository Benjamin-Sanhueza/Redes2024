import psycopg2

# Configuración de conexión
conexion = psycopg2.connect(
    host="192.168.50.1",  # Dirección IP del servidor PostgreSQL
    database="testdb",    # Nombre de la base de datos
    user="postgres",      # Usuario
    password="1234"  # Contraseña
)

# Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Ejecutar una consulta de prueba
cursor.execute("SELECT * FROM usuarios;")

# Recuperar los resultados
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Cerrar la conexión
cursor.close()
conexion.close()

