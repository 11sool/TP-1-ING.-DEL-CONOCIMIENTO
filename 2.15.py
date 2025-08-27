def calcular_promedio(*args):
    suma = sum(args)
    promedio = suma/len(args)
    print(f"el promedio es: {promedio}")

calcular_promedio(85, 90, 78, 92)