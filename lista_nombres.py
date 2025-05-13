import random

class ListaNombres:
    """
    Clase ListaNombres del Proyecto Digipymon.
    Esta clase nos servirá para gestionar las listas de Digipymons y de entrenadores enemigos.
    """
    def __init__ (self, nombres_digipymon, nombres_entrenadores):
        self.nombres_digipymon = ["Bugnix", "Larvok", "Mandiblash", "Zappinch", "Spirafly", "Chitinox", "Drilburron", "Glowmite", "Venogrit", "Scorvex", "Fungnash", "Toxibuzz", "Webdrill", "Creepuff", "Nettling", "Slinklaw","Moltwist", "Stingrowl", "Pupagoon", "Silkobrax"]

        self.nombres_entrenadores = ["Kaelor", "Tamina", "Rudrek", "Vionne", "Zark", "Elira", "Bront", "Mysha", "Kazen", "Thorne", "Luneth", "Draxil", "Selka", "Jurok", "Amari", "Fenrik", "Vessa", "Torak", "Nimelle", "Quorin"]    
        
    def obtener_nombredigipymon(self):
        return random.choice(self.nombre_digipymon)
    def obtener_nombreentrenador(self):
        return random.choice(self.nombre_entrenador)