"""
Escribir un programa que pida al usuario que introduzca una frase 
en la consola y muestre por pantalla la frase invertida.
"""


palabra = input("Dame una palabra:   ") #Dany
invertida = ""

#Por cada letra de una palabra 
for letra in palabra:
    # La primera sera la ultima, mas la segunda sera la penultima
    # Y asi se van formando la palabra invertida, es como ir enmpujando las letras
    invertida = letra + invertida
print(invertida)

"""
frase = input("Introduce una frase: ")
print(frase[::-1])
"""