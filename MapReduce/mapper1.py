with open("listado1.csv", "r") as f:
    lineas = [linea.split() for linea in f]

user = {}

for linea in lineas:
    registro = linea[0].split(";")
     
    idUser = registro[0]
    puntaje = int(registro[1])

    try:
        Acumulados = user[idUser]
        user[idUser] = Acumulados + puntaje
    except KeyError:
        user[idUser] = puntaje


maximo = max(user, key=user.get)
print(maximo)
rs = user.values()
ts = max(rs)
print(ts)
archivo_salida= maximo + ";" + str(ts) + "\n"

salida_csv = open("datos1.csv", "w")
salida_csv.write(archivo_salida)
salida_csv.close()

print("Termino ejecucion")
