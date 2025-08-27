resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def goles_temporada(resultados):
    total_anotados = 0
    total_recibidos = 0
    for equipo, goles in resultados.items():
            goles_anotados = goles[0]
            goles_recibidos = goles[1]

            total_anotados += goles_anotados
            total_recibidos += goles_recibidos
    return total_anotados, total_recibidos

goles_anotados, goles_recibidos = goles_temporada(resultados)
print(f"Goles anotados: {goles_anotados}")
print(f"Goles recibidos: {goles_recibidos}")