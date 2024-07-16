from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from utils import leer_archivo_json, guardar_datos

app = FastAPI()

ruta_archivo = 'datos/output.json'

class Gol(BaseModel):
    minuto: int
    autor: str

class Partido(BaseModel):
    id_partido: int
    grupo: str
    fecha: str
    equipo1: str
    equipo2: str
    estadio: str
    resultado: Optional[str] = None
    goles1: List[Gol] = []
    goles2: List[Gol] = []

@app.get("/consultar/{equipo}")
def consultar_datos(equipo: str):
    datos = leer_archivo_json(ruta_archivo)
    resultados = []
    for grupo in datos:
        for partido in grupo['partidos']:
            if partido['equipo1'] == equipo or partido['equipo2'] == equipo:
                resultados.append(partido)
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron datos")
    return resultados

@app.put("/modificar_resultado/{id_partido}")
def modificar_resultado(id_partido: int, resultado: str):
    datos = leer_archivo_json(ruta_archivo)
    for grupo in datos:
        for partido in grupo['partidos']:
            if partido['id_partido'] == id_partido:
                partido['resultado'] = resultado
                guardar_datos(datos, ruta_archivo)
                return partido
    raise HTTPException(status_code=404, detail="Partido no encontrado")

@app.put("/agregar_gol/{id_partido}")
def agregar_gol(id_partido: int, equipo: str, minuto: int, autor: str):
    datos = leer_archivo_json(ruta_archivo)
    for grupo in datos:
        for partido in grupo['partidos']:
            if partido['id_partido'] == id_partido:
                if partido['equipo1'] == equipo:
                    partido['goles1'].append({"minuto": minuto, "autor": autor})
                elif partido['equipo2'] == equipo:
                    partido['goles2'].append({"minuto": minuto, "autor": autor})
                else:
                    raise HTTPException(status_code=404, detail="Equipo no encontrado en este partido")
                guardar_datos(datos, ruta_archivo)
                return partido
    raise HTTPException(status_code=404, detail="Partido no encontrado")

@app.post("/crear_partido")
def crear_partido(partido: Partido):
    print(f"Datos del partido recibido: {partido}")
    datos = leer_archivo_json(ruta_archivo)
    for grupo in datos:
        if grupo['grupo'] == partido.grupo:
            grupo['partidos'].append(partido.dict())
            guardar_datos(datos, ruta_archivo)
            return partido
    raise HTTPException(status_code=404, detail="Grupo no encontrado")
  
@app.delete("/borrar_partido/{id_partido}")
def borrar_partido(id_partido: int):
    datos = leer_archivo_json(ruta_archivo)
    for grupo in datos:
        for partido in grupo['partidos']:
            if partido['id_partido'] == id_partido:
                grupo['partidos'].remove(partido)
                guardar_datos(datos, ruta_archivo)
                return {"Partido eliminado"}
    raise HTTPException(status_code=404, detail="Partido no encontrado")