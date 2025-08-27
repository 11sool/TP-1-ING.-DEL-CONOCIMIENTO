paquetes= [("Paris",200,5), ("Roma",150,4), ("Londres",180,3)]

def destinos(paquetes):
    precio_total={} #crea el diccionario dentro de la funcion
    for destino, precio, duracion in paquetes:
        precio_total[destino] = precio * duracion
        print(f"{destino}: {precio_total[destino]}")
    return precio_total

resultado= destinos(paquetes)
