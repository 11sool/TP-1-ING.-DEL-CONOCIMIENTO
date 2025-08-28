def analizar_finanzas(**kwargs):
    ingresos = []
    gastos = []
    total_gastos = 0
    total_ingresos = 0

    for key, value in kwargs.items():
        if value > 0:
            ingresos.append((key,value))
            total_ingresos += value
        else:
            gastos.append((key, value))
            total_gastos += abs(value) #los hace positivos

    if ingresos:
        print("ingresos: ")
        for key, value in ingresos: #itera sobre la tupla
            print(f"~ {key}: {value}")
        print(f"Total de ingresos: {total_ingresos}")
    if gastos:
        print("Gastos: ")
        for key, value in gastos:
            print(f"~ {key}: {value}")
        print(f"Total de gastos: {total_gastos}")

    balance_final = total_ingresos - total_gastos
    print(f"Calculo final: {balance_final}")
    return balance_final

analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)


