"""
Clase "main" del proyecto digipymon, esta será la clase base para el funcionamiento del programa
"""

from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
from lista_nombres import ListaNombres
import random

def menu_opciones():
    """
    Función que nos permitirá elegir una de las opciones de las disponibles en el videojuego.
    Todo ello se hará mediante diversos print
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

def combate(jugador):
    """
    Función que nos permitirá entrar en combate con un digipymon generado de manera aleatoria.

    Args:
        jugador (Jugador): Objeto que de la clase Jugador que representa al jugador de nuestro videojuego.
    """

    """ 
    Creamos un objeto de la clase ListaNombres() y de la clase Enemigo.
    Generamos un nombre aleatorio de la lista de nombres de digipymon con el método habilitado para ello.
    """
    lista_nombres = ListaNombres()
    enemigo = Enemigo(lista_nombres.obtener_nombreentrenador)

    #Asignamos al enemigo la cantidad de digipymons pertinente (equivalente a la nuestra)

    enemigo.cantidad_digipymon = jugador.cantidad_digipymon

    #Preguntamos al usuario por la opción a realizar:

    print("¡Elije una de las siguientes opciones!")
    print("1. Combatir")
    print("2. Huir (cuesta 1 digicoin)")
    opcion = int(input())


