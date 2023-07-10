with open("datos1.csv","r") as file:
    lineas = [linea.split() for linea in file]

with open("datos2.csv","r") as file2:
    lineas2 = [linea2.split() for linea2 in file2]

lin = lineas + lineas2
punt = {}
for linea in lin:
    registro = linea[0].split(";")

    jugador = registro[0]
    partida = int(registro[1])

    try:
        Acumulado = punt[jugador]
        punt[jugador] = Acumulado + partida
    except KeyError:
        punt[jugador] = partida

archivo_salida=''
max_key = max(punt, key=punt.get)
pt = punt.values()
max = max(pt)
archivo_salida= max_key + ";" + str(max) + "\n"

salidaArchivo = open("respuesta.csv", "w")
salidaArchivo.write(archivo_salida)
salidaArchivo.close()

print("Termino ejecucion")