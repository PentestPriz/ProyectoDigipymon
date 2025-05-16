def buscar_digipymon_aleatorio(jugador, inventario):
    digipymonObjeto = generar_digipymon_aleatorio()
    print(f"{digipymonObjeto}")
    probabilidad = 100 - (digipymonObjeto.nivel * 10)
    print(probabilidad)
    