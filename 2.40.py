estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking_notas(estudiantes):
    promedios= {}

    for estudiante, materias in estudiantes.items():
        notas = []
        for materia in materias:
            notas.extend(materias[materia])

        promedio = sum(notas) / len(notas)
        promedios[estudiante] = promedio

    #crear el ranking de mayor a menor
    ranking =sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    print("ranking de notas:")
    for i in ranking:
        print(f"{i[0]}: {i[1]}")

ranking_notas(estudiantes)
