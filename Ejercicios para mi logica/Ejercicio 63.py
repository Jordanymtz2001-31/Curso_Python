"""
Escribir un programa que reciba una cadena de caracteres y 
devuelva un diccionario con cada palabra que contiene y su frecuencia.
"""

def caracteres(text):
    text = text.split() # aqui me ayuda que se tome por palabra y no por letra
    word = {} # Creamos un diccionario
    for palabra in text:
        if palabra in word: # Si la palabra ya esta en el diccionariio, solo le sumamos uno mas
            word[palabra] += 1
        else:
            word[palabra] = 1
    return word

while True:
    try:
        print("SISTEMA DE CONETO DE PALABRAS")
        res = input("Quires probar?(si/no): ").lower()

        if res == "":
            print("Debes de colocar si o no")
        elif res == "no":
            print("Gracias por ver mi sistema")
            break
        elif res == "si":
            text = str(input("Dame un texto para contar las palabras: "))
            print(caracteres(text))
    except TypeError:
        print("Ocurrio un error en un typo de dato, debes de colocar bien")
    except Exception as e:
        print(f"Ocurrio un error en {e}\n")
        
