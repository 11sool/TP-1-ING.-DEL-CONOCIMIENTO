def registro_empleado(nombre, edad, salario, **kwargs):
    #parametros obligatorios en diccionario
    nombre = str(nombre)
    edad = int(edad)
    salario = int(salario)
    empleado = {"nombre": "Ana", "edad": 30, "salario": 3000}

    print("registro de empleado")
    for i in empleado:
        print(f"{i}: {empleado[i]}")
    for key, value in kwargs.items():
       print(f"{key}: {value}")

registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="1234567")