# Proyecto Copa América 2024 - API Cliente-Servidor

## Descripción del Proyecto
Este proyecto implementa una API para gestionar la información de los partidos de la Copa América 2024. La API permite realizar operaciones de consulta, modificación, adición y eliminación de partidos en una base de datos JSON. La API está desarrollada utilizando FastAPI y se comunica con un cliente implementado en Python utilizando la biblioteca `requests`.

## Estructura del Proyecto
El proyecto contiene los siguientes archivos principales:
- `main.py`: Script principal para iniciar el servidor.
- `usuario.py`: Script del cliente para interactuar con la API.
- `servidor.py`: Implementación de los endpoints de la API.
- `utils.py`: Utilidades para leer y escribir en el archivo JSON.
- `requirements.txt`: Archivo con dependencias a instalar.

## Requisitos Previos
- Python 3.9 o superior
- Crear un entorno virtual para alojar los archivos

## Ejecucion
Al ejecutar el script `main.py` se creará una carpeta "datos" en la cual se descargará el archivo JSON para su manipulacion. Una vez descargado el archivo se levantará el servidor. 
Nota: Se debe configurar la direccion IPv4 en el archivo `usuario.py` antes de su ejecucion.
