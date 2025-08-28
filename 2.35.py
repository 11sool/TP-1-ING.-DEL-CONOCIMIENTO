rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def optimizar_rutas(rutas, distancias_max):
    cumplen = []
    for i, ruta in enumerate(rutas):
        origen, destino, distancia =ruta
        if distancia <= distancias_max[i]:
            cumplen.append(ruta)
    print("Las rutas validas son: ")
    print(cumplen)
optimizar_rutas(rutas, distancias_max)