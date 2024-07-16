import json
import requests

def descargar_archivo_json(url, ruta_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(ruta_archivo, 'wb') as file:
            file.write(response.content)
        print('Archivo JSON descargado con éxito.')
    else:
        print('Error al descargar el archivo.')

def leer_archivo_json(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(datos, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)