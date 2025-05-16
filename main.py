"""
Clase "main" del proyecto digipymon, esta será la clase base para el funcionamiento del programa
"""

from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
from lista_nombres import ListaNombres
import random

def generar_digipymon_aleatorio():
    """
    Función que nos permitirá generar un digipymon aleatorio.
    
    Args:
        vida (int): Genera puntos de vida aleatorios entre 10 y 20.
        ataque (int): Genera puntos de ataque aleatorios entre 1 y 10.
        nivel (int): Genera un nivel aleatorio entre 1 y 3.
        tipo (str): Genera un tipo de digipymon entre fuego, agua y planta.
        nombre (str): Genera un nombre aleatorio de digipymon de la lista de digipymons.
    """
    vida = random.randint(10, 20)
    ataque = random.randint(1, 10)
    nivel = random.randint(1,3)
    tipo = random.choice("fuego", "agua", "planta")
    nombre = ListaNombres.obtener_nombredigipymon()
    
    digipymonObjeto = Digipymon(nombre, tipo, nivel, vida, ataque)
    return digipymonObjeto

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

def buscar_digipymon_aleatorio(jugador, inventario):
    digipymonObjeto = generar_digipymon_aleatorio()
    print(f"{digipymonObjeto}")
    probabilidad = 100 - (digipymonObjeto.nivel * 10)
    print(f"{probabilidad}")
