suscripciones = {
    "Jose":["mensual","anual"],
    "Ana":["mensual"]
}
def actualizar_suscripcion(suscripciones, usuario, suscripcion, **kwargs):

    if usuario in suscripciones:
        suscripciones[usuario].append(suscripcion)
    else:
        suscripciones[usuario] = [suscripcion]
        
    for usuario in suscripciones:
        print(f"{usuario}: {suscripciones[usuario]}")
    print(f"opciones adicionales de: {usuario}: {kwargs}")


actualizar_suscripcion(suscripciones,usuario="Luis", suscripcion="mensual", auto_renovacion=True)