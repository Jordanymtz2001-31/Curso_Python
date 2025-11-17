"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse 
el contenido del diccionario.
"""
dic = {}

while True:
    print("\nBIENVENIDO AL PROGRAMA DE REGISTRO DE DATOS\n")
    try:
        opcion = input("¿Quieres registrar nuevos datos? (si/no):").lower()
        if opcion == "no":
            print("Gracias por usar el programa")
            break
        elif opcion == "si":
            clave = input ("Ingrese el tipo de dato a registrar:")
            valor = input (clave + ": ")
            dic[clave] = valor # Aqui se guarda la clave en el diccionario
            print(f"\nDatos registrados correctamente: {dic}\n")
    except ValueError:
        print("Error: Debes ingresar un valor válido para la edad.")