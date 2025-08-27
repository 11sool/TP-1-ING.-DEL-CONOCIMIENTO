temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def Media(temperaturas):
    suma = sum(temperaturas)
    promedio = suma/len(temperaturas)
    print(f"Temperatura media: {promedio}")
    return promedio

def minima(temperaturas):
    minima = min(temperaturas)
    print(f"Temperatura minima: {minima}")
    return minima

def maxima(temperaturas):
    maxima = max(temperaturas)
    print(f"Temperatura maxima: {maxima}")
    return maxima

Media(temperaturas)
minima(temperaturas)
maxima(temperaturas)