nombre = input(str("Dame tu nombre: "))

def conteo(nombre):
    if nombre == "":
        return ("Dedes de ingresa un nombre")
    else:
        mayusculas = nombre.upper()
        letras = len(nombre)
    return f"\n El nombre {mayusculas} tiene {letras} letras \n"

print(conteo(nombre))