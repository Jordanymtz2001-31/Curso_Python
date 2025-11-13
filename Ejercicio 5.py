"""
Escribir un programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas el nombre 
del usuario tantas veces como el número introducido
"""

#Pedimos el nombre del usuario y numero
nombre = input("Dime tu nombre: ")
numero = int(input("Dame un nunero: "))

def conteo(nombre, numero):
    if nombre == "":  # Verifica si la cadena está vacía
        return("No puedes colocar un nombre vacio")
    else:
        return ((nombre + "\n") * numero)
    
print (conteo(nombre, numero))