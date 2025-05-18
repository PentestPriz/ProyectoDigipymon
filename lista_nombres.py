import random

class ListaNombres:
    """
    Clase ListaNombres del Proyecto Digipymon.
    Esta clase nos servirá para gestionar las listas de Digipymons y de entrenadores enemigos.
    """
    def __init__ (self):
        """
        Constructor por defecto de la clase ListaNombres

        Args:
            self: Referencia a los atributos propios
        """
        self.nombres_digipymon = ["Bugnix", "Larvok", "Mandiblash", "Zappinch", "Spirafly", "Chitinox", "Drilburron", "Glowmite", "Venogrit", "Scorvex", "Fungnash", "Toxibuzz", "Webdrill", "Creepuff", "Nettling", "Slinklaw","Moltwist", "Stingrowl", "Pupagoon", "Silkobrax"]

        self.nombres_entrenadores = ["Kaelor", "Tamina", "Rudrek", "Vionne", "Zark", "Elira", "Bront", "Mysha", "Kazen", "Thorne", "Luneth", "Draxil", "Selka", "Jurok", "Amari", "Fenrik", "Vessa", "Torak", "Nimelle", "Quorin"]    
        
    def obtener_nombredigipymon(self):
        """
        Método que nos permite obtener un nombre de Digipymon aleatorio de la lista de 20.

        Args:
            self: Referencia a los atributos propios

        Returns:
            eleccion (str): Cadena de texto que representa el nombre escogido.
        """
        eleccion = random.choice(self.nombres_digipymon)
        return eleccion
    
    def obtener_nombreentrenador(self):
        """
        Método que nos permite obtener un nombre de entrenador aleatorio de la lista de 20.

        Args:
            self: Referencia a los atributos propios

        Returns:
            eleccion (str): Cadena de texto que representa el nombre escogido.
        """

        eleccion = random.choice(self.nombres_entrenadores)
        return eleccion