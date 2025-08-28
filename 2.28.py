biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def libros(biblioteca):
    libros_2000 = []
    for titulo, info in biblioteca.items():
        if info["año"] > 2000:
            libros_2000.append(titulo)
            print(libros_2000)
            print(info)
libros(biblioteca)
