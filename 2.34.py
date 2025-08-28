encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}
def frecuencia(encuestas):
    frecuencias={}

    for pregunta, respuestas in encuestas.items():
        contador = {}

        for respuesta in respuestas:
            if respuesta in contador:
                contador[respuesta] += 1
            else:
                contador[respuesta] = 1
        frecuencias[pregunta] = contador
    print(f"{frecuencias}")

frecuencia(encuestas)
