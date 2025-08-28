
def configurar_perfiles(usuarios, **kwargs):
    perfiles={}

    for usuario in usuarios:
        perfiles[usuario] = list(kwargs.items())
    print("configuracion: ")
    print(perfiles)

usuarios = ["Ana", "Luis", "María"]
configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
