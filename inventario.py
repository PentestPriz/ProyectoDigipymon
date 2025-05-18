class Inventario:
    """
    Clase Inventario del Proyecto Digipymon.

    Nos permitirá gestionar el inventario (lugar virtual donde se guardarán los distintos objetos del videojuego
    los objetos del videojuego, los cuales modificarán los atributos de los jugadores del juego de rol).
    """

    def __init__(self):
        """
        Constructor por defecto de la clase Digipymon

        Args:
            self: Referencia a los atributos propios
        """
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        """
        Método que nos permite añadir objetos al inventario, comprobando si ya se encuentran en él.
        También nos permite incrtementar la cantidad de los mismos en caso de que ya existan.

        Args:
            self: Referencia a los atributos propios
            nombre (str): Cadena de caracteres la cual representa el nombre del objeto a agregar. Es la clave del diccionario
            cantidad (int): Número que representa la cantidad de los objetos. Actúa como contenido del diccionario.
        """

        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad

    def usar_objeto(self, nombre): 
        """
        Método que nos permite usar objetos, eliminándolos del inventario virtual (los efectos se aplicarán más tarde).

        Args:
            self: Referencia a los atributos propios.
            nombre (str): Cadena de caracteres que repesenta el nombre del objeto que utilizaremos.
        """

        if self.objetos[nombre] == 1:
            del self.objetos[nombre]
        else:
            self.objetos[nombre] -= 1
