ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def ventas_totales(ventas_mensuales):
    suma = sum(ventas_mensuales)
    promedio = suma/len(ventas_mensuales)
    print(f"el promedio es: {promedio}")

    mayor_venta = max(ventas_mensuales)
    print(f"el mes con mayor venta es: {mayor_venta}")

ventas_totales(ventas_mensuales)