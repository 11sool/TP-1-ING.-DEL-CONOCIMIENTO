def crear_perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre="Luis", edad=25, email="juan@gmail.com", ciudad="Mendoza")