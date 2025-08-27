def configurar_app(**kwargs):
    print("Configuracion: ")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)