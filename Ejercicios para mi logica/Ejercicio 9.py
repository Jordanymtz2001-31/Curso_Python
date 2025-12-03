"""
Escribir un programa que pida al usuario que introduzca una frase en la consola 
y una vocal en minúscula, y después muestre por pantalla la misma frase 
pero con la vocal introducida en mayúscula.
"""

frase = input("Dame una frase: ")
vocal = input("Dame una vocal en minuscula:")


def cambiar_vocal(frase, vocal):
    nueva_frase = ""
    if len(vocal) !=1 or not vocal.islower() or not vocal in "aeiou":
        return "Debes ingresar una sola vocal e minuscula"
    else:
        # Contamos letra por letra de la frase
        for letra in frase:
            
            # Validamos sin cada letra es una vocal
            if letra == vocal:
                # Si es una vocal entonces la convertimos a mayuscula y el += es para ir formando la nueva frase
                nueva_frase += letra.upper()
            else:
                # Si no es vocal entonces solo la agregamos tal cual
                nueva_frase += letra
        return nueva_frase
        
print(cambiar_vocal(frase, vocal))