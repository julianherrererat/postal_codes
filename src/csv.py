import gdown


url = 'https://drive.google.com/uc?id=1JzGG10Z0Lkg3WDXfiB82wWo0a6unRjVM'
output = 'coordenadas.txt'  # Cambia 'archivo_descargado.ext' al nombre que desees para el archivo descargado

gdown.download(url, output, quiet=False)
