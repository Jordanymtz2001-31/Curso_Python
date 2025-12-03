"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

def contar_letra(frase, letra):
    if frase == "" and letra == "":
        return "No se ingreso ninguna frase ni letra"
    else:
        for le in frase:
            if le == letra:
                contador = frase.count(letra)
        return f"La letra '{le}' aparece {contador} veces en la frase."
    
print(contar_letra(frase, letra))

while frase == "" and letra == "":
    print(contar_letra(frase, letra))
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
