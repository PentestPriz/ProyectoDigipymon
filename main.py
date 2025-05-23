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

    Returns:
        seleccion (int): Selección de la opción realizada.
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

    Returns:
        digipymonObjeto (Digipymon): Digipymon resultante de el proceso de la propia función.
    """
    vida = random.randint(10, 20)
    ataque = random.randint(1, 10)
    nivel = random.randint(1,3)

    lista_tipos = ["fuego", "agua", "planta"]
    tipo = random.choice(lista_tipos)

    lista_nombres = ListaNombres()
    nombre = lista_nombres.obtener_nombredigipymon()

    digipymonObjeto = Digipymon(nombre, vida, ataque, tipo, nivel)
    return digipymonObjeto





def buscar_digipymon_aleatorio(jugador, inventario):
    """
    Función buscar_digipymon_aleatorio del proyecto digipymon.
    Esta función nos permitirá atrapar a los digipymons pertinentes para poder jugar en el juego.

    Args:
        jugador (Jugador): objeto de la clase jugador que representará al jugador del juego.
        inventario (Inventario): objeto de la clase inventario que representará a nuestro jugador.
    """
    digipymonObjeto = generar_digipymon_aleatorio()
    print(f"Vas andando por la hierba alta y... ¡Un {digipymonObjeto.nombre} salvaje apareció!")
    probabilidad = 100 - (digipymonObjeto.nivel * 10)
    print(f"Tienes un {probabilidad}% de probabilidad de capturarlo...")
    bucle = True
    while bucle:
        case = int(input("¿Quieres capturar al digipymon? (Pulsa 1 si sí, cualquier otra cosa si no)"))
        if case == 1:
            if "Digipyball" in inventario.objetos and jugador.cantidad_digipymon < 6:
                inventario.usar_objeto("Digipyball")
                azar = random.randint(1, 100)
                if azar <= probabilidad:
                    print(f"¡Has capturado a {digipymonObjeto.nombre}!\n")
                    jugador.añadir_digipymon(digipymonObjeto)
                    bucle = False
                else:
                    print(f"¡No has podido capturar a {digipymonObjeto.nombre}...\n")
                    
            else:
                if "Digipyball" not in inventario.objetos:
                        print("No puedes capturar sin digipyballs...\n")
                else:
                    print("Tienes demasiados digipymon...\n")
        else:
            print("¡Has huído del combate!\n")
            bucle = False
            

def digishop(jugadorObjeto, inventario):
    """
    Función digishop del proyecto digipymon.
    Esta función nos permitirá interactuar con la tienda virtual del juego, comprando sus objetos.

    Args: 
        jugadorObjeto (Jugador): objeto de la clase Jugador que representará a nuestro jugador que comprará los objetos.
        inventario (Inventario): objeto de la clase Inventario que representará el inventario en el que se almacenarán los objetos comprados.
    """
    bucle = True
    while bucle:
        print(f"\nDigicoins disponibles: {jugadorObjeto.digicoins}")
        print("Bienvenido a la Digishop:")
        print("Pulsa 1 para comprar una digipyball                - (5 digicoins)")
        print("Pulsa 2 para comprar una poción (+10hp)            - (3 digicoins)")
        print("Pulsa 3 para comprar un anabolizante(+5dmg)        - (3 digicoins)")
        print("Pulsa 4 para salir")
        eleccion = int(input("Elige una opción...\n"))
        
        if eleccion == 1:
            if jugadorObjeto.digicoins >= 5:
                inventario.añadir_objeto("Digipyball", 1)
                jugadorObjeto.digicoins -= 5
                print("Has comprado una digipyball.")
            else:
                print("No tienes suficientes digicoins.")
                
        elif eleccion == 2:
            if jugadorObjeto.digicoins >= 3:
                inventario.añadir_objeto("Poción", 1)
                jugadorObjeto.digicoins -= 3
                print("Has comprado una poción de sanación.")
            else:
                print("No tienes suficientes digicoins.")
                
        elif eleccion == 3:
            if jugadorObjeto.digicoins >= 3:
                inventario.añadir_objeto("Anabolizante", 1)
                jugadorObjeto.digicoins -= 3
                print("Has comprado un anabolizante.")
            else:
                print("No tienes suficientes digicoins.")
                
        elif eleccion == 4:
            bucle = False
            print("¡Hasta pronto!\n")
            
        else:
            print("Opción no valida.")


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
    enemigo = Enemigo(lista_nombres.obtener_nombreentrenador())
    victorias = 0
    derrotas = 0
    control_combate = True

    #Asignamos al enemigo la cantidad de digipymons pertinente (equivalente a la nuestra).
    #Esto lo haremos mediante un bucle "for"

    for i in range(jugador.cantidad_digipymon):
        enemigo.añadir_digipymon(generar_digipymon_aleatorio())

    while control_combate:
    #Preguntamos al usuario por la opción a realizar:

        print("\n¡Elije una de las siguientes opciones!")
        print("1. Combatir")
        print("2. Huir (cuesta 1 digicoin)")
        opcion = int(input())

        #Hacemos un condicional que ejecutará el combate o lo saltará en función de la opción

        if opcion == 1:

            #Imprime el nombre del enemigo

            print(f"¡Te enfrentas contra {enemigo.nombre}!")

            #Bucle for que recorre la lista de ambos jugadores.

            for iterador in range(jugador.cantidad_digipymon):

                print(f"\n¡{jugador.nombre} saca a {jugador.lista_digipymon[iterador].nombre}!")
                print(f"¡{enemigo.nombre} saca a {enemigo.lista_digipymon[iterador].nombre}!\n")
                print(f"Tu ataque ({jugador.lista_digipymon[iterador].nombre}): {jugador.lista_digipymon[iterador].ataque}")
                print(f"Ataque de {enemigo.nombre} ({enemigo.lista_digipymon[iterador].nombre}): {enemigo.lista_digipymon[iterador].ataque}\n")
                print(f"Tu vida ({jugador.lista_digipymon[iterador].nombre}): {jugador.lista_digipymon[iterador].vida}")
                print(f"Vida de {enemigo.nombre} ({enemigo.lista_digipymon[iterador].nombre}): {enemigo.lista_digipymon[iterador].vida}\n")

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

                        print(f"La vida actual de tu digipymon es: {jugador.lista_digipymon[iterador].vida}")

                    else:

                        print(f"¡La vida de {jugador.lista_digipymon[iterador].nombre} ya se encontraba a 0!")
                        jugador.lista_digipymon[iterador].vida = 0
                        print("Por tanto, has perdido el combate...")
                        derrotas += 1

                #En caso contrario, restaremos los puntos de ataque del digipymon enemigo a la vida de nuestro digipymon actual y sumaremos 1 al contador de derrotas.

                elif jugador.lista_digipymon[iterador].ataque < enemigo.lista_digipymon[iterador].ataque:

                    if jugador.lista_digipymon[iterador].vida > 0:

                        jugador.lista_digipymon[iterador].vida = jugador.lista_digipymon[iterador].vida - enemigo.lista_digipymon[iterador].ataque

                        if jugador.lista_digipymon[iterador].vida <= 0:
                            print(f"¡La vida de {jugador.lista_digipymon[iterador].nombre} se encuentra a 0!")
                            jugador.lista_digipymon[iterador].vida = 0

                        print(f"La vida actual de tu digipymon es: {jugador.lista_digipymon[iterador].vida}")

                    else:
                        print("¡Tu vida ya se encontraba a 0, no puedes combatir!")
                    
                    print("¡Has perdido el combate!")
                    derrotas += 1


                #En caso de empate, haremos la simulación de tirar una moneda al aire, escogiendo un número entre 1 o 2 y seleccionando un aleatorio entre ellos.

                else:
                    
                    #Lógicamente esto será solo en el caso de que la vida de nuestro digipymon no sea 0, en caso contrario perderemos el combate automáticamente.

                    if jugador.lista_digipymon[iterador].vida <= 0:

                        print(f"¡La vida de {jugador.lista_digipymon[iterador].nombre} ya se encontraba a 0!")

                        derrotas += 1

                    #Quitaremos al jugador una cantidad de vida equivalente al ataque de el digipymon enemigo como en los otros casos.

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

                        jugador.lista_digipymon[iterador].vida = jugador.lista_digipymon[iterador].vida - enemigo.lista_digipymon[iterador].ataque

                        if jugador.lista_digipymon[iterador].vida <= 0:
                            print(f"¡La vida de {jugador.lista_digipymon[iterador].nombre} se encuentra a 0!")
                            jugador.lista_digipymon[iterador].vida = 0


            
            """
            Decidiremos si se gana el combate en función del número de victorias y derrotas.
            También restaremos el número de derrotas a las digicoins o sumaremos las victorias a las mismas en función de ello.
            """
            
            #Si las victorias son superiores a las derrotas se gana, en caso contrario se pierde. Si son iguales se empata.

            print(f"\nVictorias: {victorias}")
            print(f"Derrotas: {derrotas}\n")

            if victorias > derrotas:
                print(f"¡Has ganado el duelo, ganaste {victorias} digicoins!\n")
                jugador.digicoins += victorias
            elif victorias < derrotas:
                print("Has perdido el duelo...")
                if jugador.digicoins <= 0:
                    print("No te quitamos digicoins ya que no tienes ni una...\n")
                else:
                    print(f"Perdiste {derrotas} digicoins...\n")
                    jugador.digicoins -= derrotas

                    if jugador.digicoins < 0:
                        print("No tienes para pagar todo, pero te haremos el favor, anda...\n")
                        jugador.digicoins = 0
            else:
                print("Has quedado empate..., no vamos a quitarte monedas por el mal trago...\n")

            print(f"\nDigicoins actuales: {jugador.digicoins}")
            control_combate = False

        elif opcion == 2:
            if jugador.digicoins > 0:
                jugador.digicoins -= 1
                print("¡Has huído exitosamente!\n")
                control_combate = False
            else:
                print("No tienes suficientes digicoins.")

            print(f"Digicoins: {jugador.digicoins}")
        else:
            print("La opción no es válida, prueba de nuevo.")

def usar_item(jugador, inventario):
    """
    Función que nos permitirá utilizar y aprovechar los efectos de los objetos disponibles en nuestro inventario.
    
    Args:
        jugador (Jugador): Objeto de la clase jugador que representa al jugador de nuestro videojuego, el cuál utilizará los objetos.
        inventario (Inventario): Objeto de la clase inventario que nos permitirá la gestión de estos objetos.
    """

    print("Este es tu inventario: ")

    #Mostramos al jugador los digipymon que tiene
    for nombre in inventario.objetos:
        print(f"Nombre del objeto: {nombre}\nCantidad: {inventario.objetos[nombre]}\n")
    
    #Entramos en el bucle de la funcionalidad
    control_inventario = True
    while control_inventario:

        #Se pide la opción a insertar

        opcion = str(input("Escribe el nombre del objeto que deseas utilizar (Escribe Salir para salir):"))

        #Si es digipyball, no funciona

        if opcion == "Digipyball":
            print("¡No puedes usar las digipyballs fuera de encuentros!")

            if opcion not in inventario.objetos:
                print("Además, que más da, si no tienes ni una...")
        
        elif opcion == "Poción":
            
            #Comprueba si hay pociones

            if opcion not in inventario.objetos:
                print("No tienes pociones...")

            else:
                """
                En caso de que sí, muestra los digipymon que hay y les asigna un "id" a modo de iterador.

                En caso de duda acerca de por qué no se ha hecho una búsqueda por texto y después encontrar el índice mediante el método "index",
                clarificar que esto se ha hecho así debido a que es posible tener varios digipymon con un mismo nombre, así que debido a la naturaleza
                del juego, se vió más sencillo seleccionarlo en una simulación de "menú" mediante los ids, solventando asímismo el problema.
                """

                iterador = 1
                print("Estos son tus digipymon: \n")
                for digipymon in jugador.lista_digipymon:
                    print(f"{iterador}.")
                    print(digipymon.__str__())
                    iterador += 1
                
                control_numero = True
                
                #Entramos en otro bucle en el cuál preguntaremos por el id.

                while control_numero:
                    numero_digipymon = int(input("Escoge el número de tu digipymon: "))

                    #En caso de que exista, se le resta uno al id y se utiliza como índice de la lista.

                    if numero_digipymon <= len(jugador.lista_digipymon) and numero_digipymon > 0:

                        #Se sumará 10 a la vida en caso de que el id sea válido, además de restarle 1 en el inventario al objeto pertinente.

                        jugador.lista_digipymon[numero_digipymon - 1].vida += 10
                        inventario.usar_objeto(opcion)
                        print("¡Poción usada con éxito!\n")
                        
                        control_numero = False
                    else:
                        print("No has introducido un número válido, prueba de nuevo.")

        #Se repetirá la funcionalidad con el otro objeto.
        elif opcion == "Anabolizante":
            if opcion not in inventario.objetos:
                print(f"No tienes anabolizantes...")
            else:
                iterador = 1
                print("Estos son tus digipymon: \n")
                for digipymon in jugador.lista_digipymon:
                    print(f"{iterador}.")
                    print(f"- Nombre: {digipymon.nombre}")
                    print(f"- Vida: {digipymon.vida}")
                    print(f"- Ataque: {digipymon.ataque}\n")
                    iterador += 1
                
                control_numero = True
                
                while control_numero:
                    numero_digipymon = int(input("Escoge el número de tu digipymon: "))
                    if numero_digipymon <= len(jugador.lista_digipymon) and numero_digipymon > 0:
                        jugador.lista_digipymon[numero_digipymon - 1].ataque += 5
                        inventario.usar_objeto(opcion)
                        print("¡Anabolizante usado con éxito!\n")
                        control_numero = False
                    else:
                        print("No has introducido un número válido, prueba de nuevo.")

        #Desactivamos el booleano de control en caso de que se quiera salir
        elif opcion == "Salir":
            print("Saliendo...\n")
            control_inventario = False
        
        #Si la opción no es válida, se indica y se vuelve al bucle
        else:
            print("Opción no válida, prueba de nuevo...")
                

def main():
    """
    Función principal del videojuego que nos permitirá jugar al mismo.
    """

    print("¡Bienvenido al mundo de digipymon!\n")
    print("Acabas de mudarte a pueblo paleto y tu madre te está llamando, pero..., ¿A qué nombre está llamando?")

    nombre = str(input("Inserta aquí tu nombre: "))
    
    #Creamos el objeto jugador y el inventario a partir del nombre dado

    jugador = Jugador(nombre)
    inventario = Inventario()

    print(f"\nTu madre dice: ¡{nombre}, el profesor ha venido a darnos la bienvenida!")
    print("Ves al profesor con un maletín, dentro contiene una digipyball con un digipymon dentro.")
    print("Te explica que en la región existen muchos digipymons desafiantes y aventuras por vivir, de modo que te será necesario uno.")
    
    #Generamos el digipymon inicial a partir del método aleatorio.

    digipymon_inicial = generar_digipymon_aleatorio()
    jugador.añadir_digipymon(digipymon_inicial)

    print(f"¡Recibes a {digipymon_inicial.nombre}!\n")

    print("Además, te dió 3 digipyballs y una poción por esto mismo.")
    
    #Añadimos los objetos pertinentes

    inventario.añadir_objeto("Digipyball", 3)
    inventario.añadir_objeto("Poción", 1)

    print("¡Recibes digipyballs y pociones!\n")

    print(f"Ahora sí, {nombre}, empieza tu aventura...\n")
    
    #Creamos el bucle principal del videojuego
    bucle = True
    while bucle:
        seleccion = menu_opciones()
        if seleccion == 1:
            buscar_digipymon_aleatorio(jugador, inventario)
        elif seleccion == 2:
            combate(jugador)
        elif seleccion == 3:
            digishop(jugador, inventario)
        elif seleccion == 4:
            usar_item(jugador, inventario)
        elif seleccion == 5:
            print("Este es tu inventario: ")

            #Mostramos al jugador los digipymon que tiene

            if len(inventario.objetos) == 0:
                print("\nPero..., ¡Si no tienes ni un objeto!")
            else:
                for nombre in inventario.objetos:
                    print(f"Nombre del objeto: {nombre}\nCantidad: {inventario.objetos[nombre]}\n")

        elif seleccion == 6:
            jugador.consultar_digipymon()
        elif seleccion == 7:
            print("¡Adios!")
            bucle = False
        else:
            print("Opción no válida")

main()