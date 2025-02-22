# Task Manager - Gestor de Tareas en Python

Este es un programa en Python que funciona como un gestor de tareas. Permite a los usuarios crear, ver y eliminar tareas almacenadas en un archivo JSON. Es una herramienta sencilla y eficaz para gestionar tareas desde la línea de comandos.

---

## Características

- **Crear archivo de tareas**: Crea un archivo JSON para almacenar las tareas.
- **Agregar tareas**: Permite al usuario ingresar nuevas tareas con un título, descripción y fecha de creación.
- **Mostrar tareas**: Muestra todas las tareas en una tabla ordenada.
- **Eliminar tareas**: Elimina todas las tareas almacenadas en el archivo JSON.
- **Interfaz de menú**: Ofrece un menú interactivo para seleccionar las acciones a realizar.

---

## Requisitos

- Python 3.x instalado.
- Librerías adicionales:
  - `tabulate`: Para mostrar las tareas en formato de tabla.
  - `datetime`: Para registrar la fecha y hora de creación de las tareas.

Puedes instalar las librerías necesarias con el siguiente comando:
```bash
pip install tabulate

---
## Menu principal

BIENVENIDO AL TASK MANAGER
Selecciona una opcion:
1. Mostrar todas las tareas
2. Ingresar una nueva tarea
3. Eliminar todas las tareas
4. Crear archivo de tareas
5. Salir

---
##Opciones del menu

1.Mostrar todas las tareas: Muestra una tabla con todas las tareas almacenadas.

2.Ingresar una nueva tarea: Permite agregar una nueva tarea con título y descripción.

3.Eliminar todas las tareas: Borra todas las tareas del archivo JSON.

4.Crear archivo de tareas: Crea el archivo JSON si no existe.

5.Salir: Cierra el programa.


---

##Tabla de tareas

╒════╤══════════════════════╤══════════════════════════╤══════════════╤═══════════════════════╕
│    │ titulo               │ descripcion              │ completado   │ Fecha de Creacion     │
╞════╪══════════════════════╪══════════════════════════╪══════════════╪═══════════════════════╡
│  0 │ Comprar víveres      │ Ir al supermercado       │ False        │ 2023-10-05 12:34:56   │
├────┼──────────────────────┼──────────────────────────┼──────────────┼───────────────────────┤
│  1 │ Estudiar Python      │ Repasar funciones        │ False        │ 2023-10-05 13:00:00   │
╘════╧══════════════════════╧══════════════════════════╧══════════════╧═══════════════════════╛


---

##Estura de JSON

[
    {
        "titulo": "Nombre de la tarea",
        "descripcion": "Descripción de la tarea",
        "completado": false,
        "Fecha de Creacion": "2023-10-05 12:34:56"
    },
    ...
]



