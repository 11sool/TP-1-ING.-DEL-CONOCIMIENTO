puntuaciones = [("Ana",85),("Luis", 90),("Maria", 78)]

def listaOrdenada(puntuaciones):
    #ordena por el indice de mayor a menor
    puntuaciones.sort(key=lambda tupla: tupla[1], reverse=True)
    # sort modifica la lista original
    # key lambda ordena por el segundo elemento de cada tupla
    # reverse ordena de mayor a menor
    for person, puntuacion in puntuaciones:
        print(f"{person}: {puntuacion}")
    return puntuaciones

resultado=listaOrdenada(puntuaciones)