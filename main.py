from utils import descargar_archivo_json
import servidor
import os

# URL del archivo JSON en GitHub
url_github = 'https://raw.githubusercontent.com/guillericci/API_CopaAmerica/main/output.json'
ruta_archivo = 'datos/output.json'

# Descargar el archivo JSON
if not os.path.exists(ruta_archivo):
    # Crear la carpeta si no existe
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)   
    descargar_archivo_json(url_github, ruta_archivo)

# Ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("servidor:app", host="0.0.0.0", port=8000, reload = True) 
