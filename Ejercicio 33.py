palabra = input("Ingrese una palabra: ")

def letra_letra(palabra):
    if palabra == "":
        return "No se ingreso ninguna palabra"
    else:
        for letra in range(-1, -len(palabra)-1, -1):
            print(palabra[letra])
        return "Fin de la palabra"

print(letra_letra(palabra))