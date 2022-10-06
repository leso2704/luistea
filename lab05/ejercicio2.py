try:
    narchivo = input("Ingrese el nombre del archivo\n>>>")
    abrir = open(narchivo, "r", encoding="UTF-8")

    for linea in abrir:
        print(linea.upper())
except:
    print("Ingrese un archivo existente")