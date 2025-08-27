def organizar_eventos(*args):
    for i, eventos in enumerate(args,1):
        print(f"{i}. {eventos}")

organizar_eventos("Concierto","Exposición de arte", "Conferencia")