
def nueva_reserva(reservas, nombre, habitacion, precio):
    fecha = input("Ingrese la fecha que quiere reservar(yy-mm-dd): ")
    if fecha in reservas:
        for reserva in reservas[fecha]:
            if reserva[1] == habitacion:
                print(f"Habitacion {habitacion} no dicponible el {fecha}")
            return False
    else:
        reservas[fecha] = [] #no hay reserva todavia
        reservas[fecha].append((nombre,habitacion, precio))
        print(f"Reservado con exito: {nombre} en la habitacion: {habitacion} el {fecha}")
        return True

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}
nueva_reserva(reservas,nombre="Pedro", habitacion=12, precio=150)