productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

def productoMasCaro(productos):
    masCaro = productos[0]
    for productos in productos:
     if productos[1] > masCaro[1]:
        masCaro = productos

    resultado = f"El producto mas caro es: {masCaro}"
    print(resultado)

resultado = productoMasCaro(productos)