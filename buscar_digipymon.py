import random
from inventario import Inventario
from jugador import Jugador
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
            