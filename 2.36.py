inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}
def actualizar_inventario(inventario,tienda, **kwargs):
    if tienda not in inventario:
        inventario[tienda] ={}

        #actualizar
    for producto, cantidad in kwargs.items():
        if producto in inventario[tienda]:
            inventario[tienda][producto] += cantidad
        else:
            inventario[tienda][producto] = cantidad
    return inventario

resultado = actualizar_inventario(inventario,tienda="Tienda A", producto_1=10, producto_2=-5)
print(resultado)