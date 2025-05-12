class Inventario:
    """
    Clase Inventario del Proyecto Digipymon.

    Nos permitirá gestionar el inventario (lugar virtual donde guardarán
    los objetos del videojuego, los cuales modificarán los atributos de los jugadores del juego de rol).
    """

    def __init__(self):
        """
        Constructor por defecto de la clase Digipymon

        Args:
            self: Referencia a los atributos propios
        """
        self.objetos = {}

    