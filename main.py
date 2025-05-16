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





def buscar_digipymon_aleatorio(Jugador, Inventario):
    digipymonObjeto = generar_digipymon_aleatorio()
    print(f"{digipymonObjeto}")
    probabilidad = 100 - (digipymonObjeto.nivel * 10)
    print(f"{probabilidad}")
    bucle = True
    while bucle:
        case = int(input("------"))
        if case == 1:
            if "Digipyball" in Inventario.añadir_objeto["Digipyball"]:
                Inventario.usar_objeto("Digipyball")
                azar = random.randint(1, 100)
                if azar <= probabilidad:
                    Jugador.añadir_digipymon(digipymonObjeto)
                else:
                    print("No tienes digipyballs")
            else:
                bucle = False
            
            
            
            
            




def digishop(jugadorObjeto: Jugador, inventario: Inventario):
    bucle = True
while bucle:
    print("Bienvenido a la Digishop:")
    print("Pulsa 1 para comprar una digipyball                - (5 digicoins)")
    print("Pulsa 2 para comprar una poción de sanación(+10hp) - (3 digicoins)")
    print("Pulsa 3 para comprar un anabolizante(+5dmg)        - (3 digicoins)")
    print("Pulsa 4 para salir")
    eleccion = int (input())
    
    if eleccion == 1:
        if Jugador.consultar_digicoins >= 5:
            Inventario.añadir_objeto("digipyballs", 1)
            Jugador.consultar_digicoins = -5
            print("Has comprado una digipyball.")
        else:
            print("No tienes suficientes digicoins.")
            
    elif eleccion == 2:
        if Jugador.consultar_digicoins >= 3:
            Inventario.añadir_objeto("poción de sanación", 1)
            Jugador.consultar_digicoins = -3
            print("Has comprado una poción de sanación.")
        else:
            print("No tienes suficientes digicoins.")
            
    elif eleccion == 3:
        if Jugador.consultar_digicoins >= 3:
            Inventario.añadir_objeto("anabolizante", 1)
            Jugador.consultar_digicoins = -3
            print("Has comprado un anabolizante.")
        else:
            print("No tienes suficientes digicoins.")
            
    elif eleccion == 4:
        bucle = False
        print("Hasta pronto.")
        
    else:
        print("Opción no valida.")
    
    
            


