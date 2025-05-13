import random

class clase_ListaNombres:
    """
    Clase ListaNombres del Proyecto Digipymon.
    Esta clase nos servirá para gestionar las listas de Digipymons y de entrenadores enemigos.
    """
    def __init__ (self, nombres_digipymon, nombres_entrenadores):
        """
         Constructor por parámetros de la clase ListaNombres.

         Args:
            nombres_digipymon (str): Cadena de texto donde se muestran los nombres de los diferentes 20 digipymons del juego.
            nombres_entrenadores (str): Cadena de texto donde se muestran los nombres de los diferentes 20 entrenadores del juego.
        """
        self.nombres_digipymon = ["Bugnix", "Larvok", "Mandiblash", "Zappinch", "Spirafly", "Chitinox", "Drilburron", "Glowmite", 
                                  "Venogrit", "Scorvex", "Fungnash", "Toxibuzz", "Webdrill", "Creepuff", "Nettling", "Slinklaw",
                                  "Moltwist", "Stingrowl", "Pupagoon", "Silkobrax"]

        self.nombres_entrenadores = ["Kaelor", "Tamina", "Rudrek", "Vionne", "Zark", "Elira", "Bront", "Mysha", "Kazen", "Thorne", 
                                     "Luneth", "Draxil", "Selka", "Jurok", "Amari", "Fenrik", "Vessa", "Torak", "Nimelle", "Quorin"]    
        
    def obtener_nombredigipymon(self):
        """
        Método que nos permite obtener un nombre de Digipymon aleatorio de la lista de 20.

        Args:
            self: Referencia a los atributos propios
        """
        return random.choice(self.nombre_digipymon)
    def obtener_nombreentrenador(self):
        """
        Método que nos permite obtener un nombre de entrenador aleatorio de la lista de 20.

        Args:
            self: Referencia a los atributos propios
        """
        return random.choice(self.nombre_entrenador)