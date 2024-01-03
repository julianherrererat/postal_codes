##################################################
#
# Esta funcnion descarga el archivo desde google drive 
#       y luego lo carga a la base de datos definida desde el servicio
#
##################################################

import gdown
import pandas as pd


# Funcion para descargar el archivo en drive con la libreria gdonw

def descargar_csv(id):
    url = f'https://drive.google.com/uc?id={id}'
    output = 'coordenadas.txt'  
    try:
        gdown.download(url, output, quiet=False)
    except:
        print('El Archivo no existe')

