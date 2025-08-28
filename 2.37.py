hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def repetidos(hashtags, tendencias, frecMin):
    Moda = []
    for hashtag in hashtags:
        if hashtag in Moda: #revisar si se repite el hashtag
            continue
        for hasht, frecuencia in tendencias:
            if hasht == hashtag and frecuencia > frecMin: #si supera el minimo requerido
                Moda.append(hashtag)
                break

    print(Moda)
repetidos(hashtags, tendencias, frecMin=100)
