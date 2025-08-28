def simular_ventas(*args):
    ingresos = {}
    print("Ingresos por productos: ")
    for producto, ventas, precio in args:
        ingresos[producto] = ventas * precio
        print(f"{producto}: {ingresos[producto]}")
    ingresos_totales = sum(ingresos.values())
    print(f"Ingresos totales: {ingresos_totales}")
    return ingresos
simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))