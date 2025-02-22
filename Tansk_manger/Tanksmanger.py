import json
from tabulate import tabulate
from datetime import datetime
import time as tm
import os

nombre_archivo = "tareas.json"

# Obtener la ruta del archivo donde está el script Python
ruta_actual = os.path.dirname(os.path.abspath(__file__))
# Crear el archivo JSON en la misma carpeta del script
ruta_archivo = os.path.join(ruta_actual, nombre_archivo)


# Funcion para verificar si existe el archivo json donde se guardan las tareas y si no existe pues lo crea
def si_existe():
    # Comprobar si el archivo existe
    if not os.path.exists(ruta_archivo):
        # Si no existe, crear el archivo JSON con un contenido vacío o el que desees
        with open(ruta_archivo, 'w') as contenido:
            json.dump([], contenido)
            print(f'Archivo "{ruta_archivo}" creado con éxito.')
            tm.sleep(2)
            # Esto es para Windows; puedes omitir si no usas Windows
            os.system("cls")

    else:
        print(f'El archivo "{ruta_archivo}" ya existe.')
        tm.sleep(2)
        os.system("cls")

# Funcion para ingresar una nueva tarea al json


def n_resgitro():
    try:
        with open(ruta_archivo, "r") as contenido:
            datos = json.load(contenido)
    except (OSError, FileNotFoundError):
        print("ERROR | no se encuentra el archivo")
        return

    nombre = input("Ingresar nombre tarea -> ")
    descripcion = input("Ingresar descripcion de la tarea -> ")
    estado = False

    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    nueva_tarea = {
        "titulo": nombre,
        "descripcion": descripcion,
        "completado": estado,
        "Fecha de Creacion": hora
    }

    datos.append(nueva_tarea)
    with open(ruta_archivo, "w") as contenido:
        json.dump(datos, contenido, indent=4)
    print("Tarea Agregada")

# Funcion para mostrar todas las tares en el  json


def mostrar_registros():
    try:
        with open(ruta_archivo, "r") as contenido:
            datos = json.load(contenido)
    except (OSError, FileNotFoundError):
        print("ERROR | no se encuentra el archivo")
        print("Primero Crealo con la opcion 4")
        tm.sleep(1.5)
        os.system("cls")
        return

    if not datos:
        print("-----------NO HAY TAREAS------------ ".center(50))
    else:
        print(tabulate(datos, headers="keys", showindex=True, tablefmt="fancy_grid"))
        # Funciona en Windows, puede eliminarse si usas Linux o macOS
        os.system("pause")
        os.system("cls")


# Funcion para eleminar todas las tareas del Json
def eleminar_registro():
    with open(ruta_archivo, "r") as archivo:
        datos = json.load(archivo)

    datos.clear()  # Borrar todo el contenido

    with open(ruta_archivo, "w") as contenido:
        json.dump(datos, contenido, indent=4)

    print("SE HA BORRADO TODO JAJAJAJA")
    tm.sleep(1)
    os.system("cls")


# Funcion la cual ejecutara todas las funciones anteriores
def menu():
    while True:
        print("""BIENVENIDO AL TASK MANAGER
          Selecciona una opcion:
          1. Mostrar todas las tareas
          2. Ingresar una nueva tarea
          3. Eliminar todas las tareas
          4. Crear archivo de tareas
          5. Salir
          """)
        tm.sleep(1)
        try:
            seleccion = int(input("Ingresar Opcion -> "))
        except ValueError:
            print("ERROR: Debes ingresar un número válido.")
            tm.sleep(2)
            os.system("cls")
            continue

        if seleccion == 1:
            os.system("cls")
            mostrar_registros()

        elif seleccion == 2:
            os.system("cls")
            n_resgitro()

        elif seleccion == 3:
            os.system("cls")
            eleminar_registro()

        elif seleccion == 5:
            print("ESTÁS SALIENDO")
            tm.sleep(1.5)
            os.system("cls")
            break

        elif seleccion == 4:
            os.system("cls")
            si_existe()

        else:
            print(
                f"ERROR -> ({seleccion}) / Ingresar una de las opciones válidas")
            tm.sleep(2)
            os.system("cls")


menu()
