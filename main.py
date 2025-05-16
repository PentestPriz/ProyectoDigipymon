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

def combate(jugador=Jugador("Josito")):
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
    victorias = 0
    derrotas = 0


    #Asignamos al enemigo la cantidad de digipymons pertinente (equivalente a la nuestra).
    #Esto lo haremos mediante un bucle "for"

    for i in range(6):
        enemigo.añadir_digipymon(digipymon=Digipymon(lista_nombres.obtener_nombredigipymon(), random.randint(10, 20), random.randint(10, 20), "Planta", 15))
        jugador.añadir_digipymon(digipymon=Digipymon(lista_nombres.obtener_nombredigipymon(), random.randint(10, 20), random.randint(10, 20), "Planta", 15))

    #Preguntamos al usuario por la opción a realizar:

    print("¡Elije una de las siguientes opciones!")
    print("1. Combatir")
    print("2. Huir (cuesta 1 digicoin)")
    opcion = int(input())

    #Hacemos un condicional que ejecutará el combate o lo saltará en función de la opción

    if opcion == 1:

        #Imprime el nombre del enemigo

        print(f"¡Te enfrentas contra {enemigo.nombre}!")

        #Bucle for que recorre la lista de ambos jugadores.

        for iterador in range(jugador.cantidad_digipymon):

            print(f"¡{jugador.nombre} saca a {jugador.lista_digipymon[iterador].nombre}!")
            print(f"¡{enemigo.nombre} saca a {enemigo.lista_digipymon[iterador].nombre}!")

            """
            Si nuestro ataque es mayor, entonces nuestro digipymon ganará el combate.
            Restaremos los puntos de ataque del digipymon enemigo a la vida de nuestro digipymon actual y y sumará 1 al contador de victorias.
            """

            if jugador.lista_digipymon[iterador].ataque > enemigo.lista_digipymon[iterador].ataque:

                if jugador.lista_digipymon[iterador].vida > 0:
                    jugador.lista_digipymon[iterador].vida = jugador.lista_digipymon[iterador].vida - enemigo.lista_digipymon[iterador].ataque
                    print("¡Has ganado el combate!")
                    victorias += 1

                    if jugador.lista_digipymon[iterador].vida <= 0:
                        print(f"¡La vida de {jugador.lista_digipymon[iterador].nombre} se encuentra a 0!")
                        jugador.lista_digipymon[iterador].vida = 0

                else:

                    print(f"¡La vida de {jugador.lista_digipymon[iterador].nombre} se encuentra a 0!")
                    jugador.lista_digipymon[iterador].vida = 0
                    print("Por tanto, has perdido el combate...")
                    derrotas -= 1

            #En caso contrario, restaremos los puntos de ataque del digipymon enemigo a la vida de nuestro digipymon actual y sumaremos 1 al contador de derrotas.

            elif jugador.lista_digipymon[iterador].ataque < enemigo.lista_digipymon[iterador].ataque:

                if jugador.lista_digipymon[iterador].vida > 0:
                    jugador.lista_digipymon[iterador].vida = jugador.lista_digipymon[iterador].vida - enemigo.lista_digipymon[iterador].ataque
                else:
                    print("¡Tu vida se encuentra a 0!")
                    jugador.lista_digipymon[iterador].vida = 0
                print("¡Has perdido el combate!")
                derrotas += 1

            #En caso de empate, haremos la simulación de tirar una moneda al aire, escogiendo un número entre 1 o 2 y seleccionando un aleatorio entre ellos.

            else:
                print("¡Nos encontramos ante un empate!")
                cara_escogida = int(input("Selecciona entre cara o cruz (1 o 2):"))
                cara_resultante = random.randint(1, 2)
                if cara_escogida == cara_resultante:
                    print("¡Ganaste el combate!")
                    victorias += 1
                elif cara_escogida != cara_resultante:
                    print("Has perdido el combate...")
                    derrotas += 1
                else:
                    print("Has introducido una opción no válida, y perdido el combate por ello...")
                    derrotas += 1

                #Quitaremos al jugador una cantidad de vida equivalente al ataque de el digipymon enemigo como en los otros casos.
                if jugador.lista_digipymon[iterador].vida > 0:
                    jugador.lista_digipymon[iterador].vida = jugador.lista_digipymon[iterador].vida - enemigo.lista_digipymon[iterador].ataque
                else:
                    print(f"¡La vida de {jugador.lista_digipymon[iterador].nombre} se encuentra a 0!")
                    jugador.lista_digipymon[iterador].vida = 0
        
        """
        Decidiremos si se gana el combate en función del número de victorias y derrotas.
        También restaremos el número de derrotas a las digicoins o sumaremos las victorias a las mismas en función de ello.
        """
        
        #Si las victorias son superiores a las derrotas se gana, en caso contrario se pierde. Si son iguales se empata.

        if victorias > derrotas:
            print(f"¡Has ganado el duelo, ganaste {victorias} digicoins!")
            jugador.digicoins += victorias
        elif victorias < derrotas:
            print("Has perdido el duelo...")
            if jugador.digicoins < 0:
                print("No te quitamos digicoins ya que no tienes ni una...")
            else:
                print(f"Has perdido el duelo, ganaste {derrotas} digicoins...")
                jugador.digicoins -= derrotas
        else:
            print("Has quedado empate..., no vamos a quitarte monedas por el mal trago...")

        print(f"Digicoins: {jugador.digicoins}")

    elif opcion == 2:
        print("¡Has huído del combate!")
        jugador.digicoins -= 1
    else:
        print("La opción no es válida, prueba de nuevo.")

combate(jugador=Jugador("Josito"))

