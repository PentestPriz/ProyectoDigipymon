def generar_digipymon_aleatorio():
    """
    Función que nos permitirá generar un digipymon aleatorio.
    """
    vida = random.randint(10, 20)
    ataque = random.randint(1, 10)
    nivel = random.randint(1,3)
    tipo = random.choice("fuego", "agua", "planta")
    nombre = lista.obtener_nombre_digipymon()
    
    return digipymon(nombre, tipo, nivel, vida, ataque)
 