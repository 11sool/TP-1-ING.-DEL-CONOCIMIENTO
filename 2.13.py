estudiantes = dict({
    101: {"Nombre":"Ana", "Edad":16, "calificaciones":{"matemáticas":8.5, "ciencias":9.0}},
    102:{"Nombre":"Luis", "Edad":17, "calificaciones":{"matemáticas":7.8, "ciencias":8.8}}
})

def registro(estudiantes):
    clave = int(input("Ingrese clave: "))

    if clave not in estudiantes:
        print("Usuario no encontrado")
        return None

    estudiante = estudiantes[clave]
    calificaciones = estudiante["calificaciones"]

#calcular promedio
    suma = sum(calificaciones.values())
    cantidad = len(calificaciones)
    promedio = suma / cantidad

    print(" ")
    print(f"Nombre: {estudiante["Nombre"]}")
    print("Calificaciones:")
    for materia, nota in calificaciones.items():
        print(f" -{materia}: {nota}")
    print(f"Promedio : {promedio}")

    return promedio

resultado = registro(estudiantes)