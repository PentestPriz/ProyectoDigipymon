class enemigo:
    """
    Clase Enemigo del proyecto Digipymon.
    La clase se encargará de la gestión de enemigos  y la asociación con sus digipymons.
    """
    def __init__(self, nombre):
        """
        Constructor por parámetros de la clase Digipymon.
        
        Args:
            self: Referencia a los atributos propios.
            nombre (str): Cadena de caracteres que representa el nombre del enemigo
        """
        self.nombre = (nombre)
        lista_digipymon = []
        cantidad_digipymon = 0
    
    def añadir_digipymon(self, digipymon):
        """
        Método para añadir digipymons al enemigo, sumándolos a su lista.

        Args:
            self: Referencia a los atributos propios.
            digipymon (Digipymon): Objeto de la clase Digipymon que añadiremos al enemigo.
        """
        self.lista.digipymons(digipymon)
        self.cantidad.digipymon = digipymon + 1