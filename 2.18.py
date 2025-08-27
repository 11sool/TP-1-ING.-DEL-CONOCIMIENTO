ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def total_ventas(ventas_diarias):
    total = sum(ventas_diarias)
    promedio = total/len(ventas_diarias)
    print(f"Total de ventas: {total}")
    print(f"Promedio de ventas diarias: {promedio}")

total_ventas(ventas_diarias)