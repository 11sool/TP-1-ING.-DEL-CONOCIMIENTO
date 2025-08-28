precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0),
               ("venta", 3),
               ("compra", 2),
               ("venta", 4)]

def acciones(precios_diarios, operaciones):
    total = 0
    pecio_compra = 0

    for tipo, dia in operaciones:
        if tipo == "compra":
            precio_compra = precios_diarios[dia]
            print(f"precio {tipo} {precio_compra}")
        else:
            tipo == "venta"
            precio_venta = precios_diarios[dia]
            ganancia = precio_venta - precio_compra
            total += ganancia
            print(f"precio {tipo} {precio_venta}, ganancia: {ganancia}")
    print(f"Ganancia total: {total}")

acciones(precios_diarios, operaciones)