import mysql.connector


# Conexión a la base de datos MySQL
connection = mysql.connector.connect(
    host='0.0.0.0',  # Cambiar por la dirección de tu servidor MySQL
    user='root',  # Cambiar por tu usuario
    password='bia',  # Cambiar por tu contraseña
    database='codigos_postales',  # Cambiar por el nombre de tu base de datos
    port='33060'
)

# Función para insertar datos en la base de datos MySQL
def insertar_datos(datos):
    cursor = connection.cursor()

    # Reemplaza 'coordenadas' por el nombre de tu tabla
    tabla = 'coordenadas'

    # Insertar datos en la tabla de la base de datos
    for index, row in datos.iterrows():
        longuitud = row['lon']
        latitud = row['lat']

        # Inserta los valores de 'longitud' y 'latitud' en tu tabla, junto con un ID autoincremental
        query = f"INSERT INTO {tabla} (latitud, longuitud) VALUES (%s, %s)"
        cursor.execute(query, (latitud, longuitud))

    connection.commit()
    cursor.close()

# Insertar los datos en la base de datos

# Cerrar la conexión a la base de datos
    connection.close()
