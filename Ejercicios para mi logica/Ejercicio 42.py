def palindromo(palabra):
        invertida = ""
        for l in palabra:
            invertida = l + invertida
        if palabra == invertida:
            return f"La palabra {palabra} es un palindromo" 
        else:
            return f"La palabra {palabra} no es un palindromo"
            

while True:
    palabra = input("Dame una palabra: ").lower()
    if palabra == "":
            print("No se ingreso ninguna palabra")
    elif palabra != "salir":
            print(palindromo(palabra))
    else:
        palabra == "salir"
        break


    
    