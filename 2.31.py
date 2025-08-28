def publicar(nombre,texto,**kwargs):
   nombre=str(nombre)
   texto=str(texto)
   publicacion = {"nombre":"Juan", "texto":"Mi primer post!"}

   for i in publicacion:
       print(f"{i}: {publicacion[i]}")

   for key, value in kwargs.items():
       print(f"{key}: {value}")

publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)