"""
Clase "main" del proyecto digipymon, esta será la clase base para el funcionamiento del programa
"""

from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
import random

def menu_opciones():
    """
    Función que nos permitirá elegir una de las opciones de las disponibles en el videojuego.
    """

    print("Escoja una de las siguientes opciones: ")
    print("1. Buscar un digipymon.")
    print("2. Luchar contra un entrenador.")
    print("3. Ir a la tienda.")
    print("4. Usar objetos.")
    print("5. Consultar inventario.")
    print("6. Consultar digipymons")
    print("7. Salir.")

    seleccion = int(input("Introduzca su opción aquí: "))

    return seleccion


