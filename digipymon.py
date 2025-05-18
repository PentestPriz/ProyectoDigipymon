class Digipymon:
    """
    Clase Digipymon del Proyecto Digipymon.
    Esta clase nos servirá para instanciar a modo de objeto las criaturas virtuales conseguidas durante el videojuego.
    """

    def __init__(self, nombre, vida, ataque, tipo, nivel):
        """
        Constructor por parámetros de la clase Digipymon.

        Args:
            nombre (str): Cadena de texto que representa el nombre de la criatura virtual.
            vida (int): Número entero que representa la vida que tendrá nuestra criatura.
            ataque (int): Número entero que representa los puntos de ataque (daño que realizará a otras criaturas) de nuestra criatura.
            tipo (str): Cadena de texto que representa el tipo que tendrá (el elemento que domina) nuestra criatura.
            nivel (int): Número entero que representa el nivel de nuestro Digipymon.
        """

        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        """
        Método que nos permitirá la impresión por consola de los distintos atributos de nuestra clase Digipymon.

        Args:
            self: Referencia a los atributos propios.

        Returns:
            stats (str): Cadena de texto con las características de nuestro digipymon.
        """
        
        stats = f"Nombre del digipymon: {self.nombre}\nVida del digipymon: {self.vida}\nAtaque del digipymon: {self.ataque}\nTipo del digipymon: {self.tipo}\nNivel del digipymon: {self.nivel}\n"
        return stats