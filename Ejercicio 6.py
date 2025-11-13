"""
Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces, 
una con todas las letras minúsculas, otra con todas las letras mayúsculas y 
otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

nombre = input("Dame tu nombre completo:")

def convertidor(nombre):

    if nombre == "":
        return ("No puede dejar vacio el nombre")
    else:
        mayuscula = nombre.upper()
        minuscula = nombre.lower()
        nombre_completo= nombre.title()
    return f"Los nombre son {mayuscula}\n{minuscula}\n{nombre_completo}"

print(convertidor(nombre))