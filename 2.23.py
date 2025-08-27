inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def inventario_actualizado(inventario, ventas):
    actualizado = []

    for i in range (len(inventario)):
        nuevo_inventario = inventario[i] - ventas[i]
        actualizado.append(nuevo_inventario)
        #append agrega un elemento al final de la lista
    return actualizado
resultado = inventario_actualizado(inventario, ventas)

print(f"Inventario actualizado: {resultado}")