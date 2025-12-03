while True: # Es decir que el bucle se ejecutara siempre
    frase = input("Ingrese una frase: ")
    if frase == "": # Si la frase esta vacia
        print("No se ingreso ninguna frase")
    elif frase == "salir":
        break # Salir del bucle
    print(f"La frase ingresada es: {frase}")
