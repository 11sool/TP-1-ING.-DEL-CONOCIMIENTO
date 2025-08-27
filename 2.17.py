empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("Maria", 35, 4000)
}
empleado =empleados[1]
nombre = empleado[0]
edad = empleado[1]
salario = empleado[2]

def mayor_salario(empleados, salarioMin):
    resultado = {} #inicializar
    for id, datos in empleados.items():
        salario = datos[2] #salario en la tupla
        if salario > salarioMin:
            resultado[id] = datos
    return resultado

resultado = mayor_salario(empleados, 2700)
print(resultado)