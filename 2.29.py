notas_estudiantes = [("Ana",[85,90,78]),("Luis",[88,92,80]),("Maria",[75,85,70])]

def calculo_promedios(notas_estudiantes):
    promedios = {}
    for estudiante, calificaciones in notas_estudiantes:
        suma = sum(calificaciones)
        promedio = suma / len(calificaciones)
        promedios[estudiante] = promedio
        print(f"Estudiante: {estudiante}, Promedio: {promedio}")
    return promedios

calculo_promedios(notas_estudiantes)
