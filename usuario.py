import requests

base_url = "http://192.168.100.144:8000"

def consultar_datos(equipo):
    url = f"{base_url}/consultar/{equipo}"
    response = requests.get(url)
    return response.json()

def modificar_resultado(id_partido, resultado):
    url = f"{base_url}/modificar_resultado/{id_partido}"
    response = requests.put(url, params={"resultado": resultado})
    return response.json()

def agregar_gol(id_partido, equipo, minuto, autor):
    url = f"{base_url}/agregar_gol/{id_partido}"
    response = requests.put(url, params={"equipo": equipo, "minuto": minuto, "autor": autor})
    return response.json()

def crear_partido(partido):
    url = f"{base_url}/crear_partido"
    response = requests.post(url, json=partido)
    return response.json()
    
def borrar_partido(id_partido):
    url = f"{base_url}/borrar_partido/{id_partido}"
    response = requests.delete(url)
    return response.json()

if __name__ == "__main__":
    
    while True: 
        print("Menu de opciones:  ")
        print("1. Consultar resultados")
        print("2. Modificar resultado")
        print("3. Agregar gol")
        print("4. Crear partido")
        print("5. Borrar partido")
        print("6. Salir")
        opc = input("Ingrese una opcion: ")
        if opc == '1': 
            # Ejemplo de consulta
            equipo = str(input("Ingrese equipo de futbol: "))
            resultados = consultar_datos(equipo)
            print(resultados)

        elif opc == '2':
            # Ejemplo de modificación de resultado
            id = int(input("Ingrese el id del partido: "))
            resul = str(input("Ingrese el resultado: "))
            modificacion = modificar_resultado(id, resul)
            print(modificacion)

        elif opc == '3':
            # Ejemplo de agregar gol
            id = int(input("Ingrese el id del partido: "))
            equipo = str(input("Ingrese equipo de futbol: "))
            min = int(input("Ingrese los minutos del gol: "))
            jugador = str(input("Ingrese el autor del gol: "))
            gol = agregar_gol(id, equipo, min, jugador)
            print(gol)

        elif opc == '4':
            #Crear partido
            id = int(input("Ingrese el ID del partido: "))
            grupo = input("Ingrese el grupo: ")
            fecha = input("Ingrese la fecha del partido 'AAAA-MM-DD': ")
            equipo1 = input("Ingrese equipo 1: ")
            equipo2 = input("Ingrese equipo 2: ")
            estadio = input("Ingrese el estadio de futbol: ")
            partido = {
                "id_partido": id,
                "grupo": grupo,
                "fecha": fecha,
                "equipo1": equipo1,
                "equipo2": equipo2,
                "estadio": estadio,
                "resultado": None,
                "goles1": [],
                "goles2": []
            }
            creacion = crear_partido(partido)
            print(creacion)
        elif opc == '5':
             #Borrar partido
            id_partido = int(input("Ingrese ID del partido: "))
            borrado = borrar_partido(id_partido)
            print(borrado)
        elif opc == '6':
            break
        else:
            print("Opcion no valida")
        