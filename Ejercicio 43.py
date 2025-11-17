def busqueda_vocal(palabra, vocal):
    contador = 0
    for letra in palabra:
        if letra == vocal:
            contador += 1
    return f"La vocal '{vocal}' se encuentra {contador} veces en la palabra '{palabra}'"

while True:
    palabra = input("Dame una palabra: ").lower()
    if palabra == "":
        print("No se ingreso ninguna palabra")
    elif palabra != "salir":
        vocal = input("Dame una vocal para buscar en la palabra: ").lower()
        if vocal in "aeiou" and len(vocal) == 1:
            print(busqueda_vocal(palabra, vocal))
        else:
            print("No ingresaste una vocal valida o ingresastes dos o mas vocales.")
    elif palabra == "salir":
        break