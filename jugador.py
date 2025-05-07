#Clase Jugador del proyecto Digipymon
#La clase se encargará de la gestión de jugadores y la asociación con sus digipymons

class Jugador:
    #Constructor por parámetros de la clase jugador
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    #Método que nos añade un digipymon a la lista y lo suma a la cantidad total
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon = self.cantidad_digipymon + 1
    