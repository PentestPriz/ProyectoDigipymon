#Clase Jugador del proyecto Digipymon
#La clase se encargará de la gestión de jugadores y la asociación con sus digipymons

class Jugador:
    #Constructor por parámetros de la clase jugador.
    def __init__(self, nombre):
        self.nombre = nombre
        lista_digpymon = []
        cantidad_digipymon = 0
        digicoins = 10

    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.apend(digipymon)
        cantidad_digipymon = cantidad_digipymon + 1
            