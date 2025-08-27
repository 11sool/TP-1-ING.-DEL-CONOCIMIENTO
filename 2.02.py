datos = [["A", "B", "C"],
         ["D", "E", "F"],
         ["G", "H", "I"]]

for i in range(len(datos)):
    for j in range(len(datos)):
        print(datos[i][j], end="")
    print(" ")
