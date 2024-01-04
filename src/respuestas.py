
import mysql.connector
from sqlalchemy import create_engine
import json
from decimal import Decimal


# Configuración de la conexión a la base de datos MySQL
db_config = {
    'host': '0.0.0.0',  # Cambiar por la dirección de tu servidor MySQL
    'user': 'root',  # Cambiar por tu usuario
    'password': 'bia',  # Cambiar por tu contraseña
    'database': 'codigos_postales',  # Cambiar por el nombre de tu base de datos
    'port': '33060'
}

def resultado():
    
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM codigos_postales.errores;")
    errores = cursor.fetchall()
    
    column_names = [i[0] for i in cursor.description]

# Convertir los resultados a una lista de diccionarios
    errores_list = []
    for error in errores:
        error_dict = dict(zip(column_names, error))
        
        # Convertir valores 'Decimal' a 'float'
        for key, value in error_dict.items():
            if isinstance(value, Decimal):
                error_dict[key] = float(value)

        errores_list.append(error_dict)


# Convertir a formato JSON
    errores_json = json.dumps(errores_list)

    return(errores_json)

def resultado_data():

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("""select T1.id id_coordenada ,concat(T1.latitud,',',T1.longuitud) as lat_long_csv,T0.postcode,concat(T0.latitude,',',T0.longitude)as lat_long_postcode , T0.distance 
	 from codigos_postales T0 join codigos_postales.coordenadas T1 on T0.fk_id = T1.id;""")
    datos = cursor.fetchall()
    
    column_names = [i[0] for i in cursor.description]

# Convertir los resultados a una lista de diccionarios
    resultado_data_list = []
    for data in datos:
        data_dict = dict(zip(column_names, data))
        
        # Convertir valores 'Decimal' a 'float'
        for key, value in data_dict.items():
            if isinstance(value, Decimal):
                data_dict[key] = float(value)

        resultado_data_list.append(data_dict)


# Convertir a formato JSON
    data_json = json.dumps(resultado_data_list)

    return(data_json)
