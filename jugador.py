class Jugador:
    """
    Clase Jugador del proyecto Digipymon.
    La clase se encargará de la gestión de jugadores y la asociación con sus digipymons.
    """
    def __init__(self, nombre):
        """
        Constructor por parámetros de la clase Digipymon.
        
        Parameters:
        self: Referencia a los atributos propios.
        nombre (str): Cadena de caracteres que representa el nombre del jugador
        """
        self.nombre = nombre
        lista_digpymon = []
        cantidad_digipymon = 0
        digicoins = 10


    def añadir_digipymon(self, digipymon):
        """
        Método para añadir digipymons al jugador, sumándolos a su lista.

        Parameters:
        self: Referencia a los atributos propios.
        digipymon (Digipymon): Objeto de la clase Digipymon que añadiremos al jugador.
        """
        self.lista_digipymon.apend(digipymon)
        cantidad_digipymon = cantidad_digipymon + 1

    def consultar_digipymon(self, digipymon):
        """
        Método para consultar la lista de digipymons, recorriéndola e imprimiñendola.

        Parameters:
        self: Referencia a los atributos propios.
        digipymon (Digipymon): Objeto de la clase Digipymon que añadiremos al jugador
        """
        print("Estos son todos tus digipymon.")
        for iterador in digipymon:
            print("- " + iterador)
        print("Vaya..., esas son más criaturas que las disponibles en cierta saga de videojuegos...")