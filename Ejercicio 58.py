"""
Escribir una función que reciba una muestra de números en una lista y 
devuelva su media, varianza y desviación típica en un diccionario.
"""
# Funcion para calcular el numero intermedio de una lista
def intermedio(lis_numeros):
    media = sum(lis_numeros) / len(lis_numeros)
    return media
        
while True:
    try:
        print("\nBIENVENIDO AL PROGRAMA DE NÚMEROS INTERMEDIOS")
        res = str(input("¿Desea ingresar una lista de números? (si/no): ")).lower()
        if res == "no":
            print("Gracias por usar el programa")
            break
        elif res != "si" and res != "no":
            print("Respuesta no valida. Por favor ingrese 'si' o 'no'.\n")
        elif res == "si":
            entrada = input("Ingrese una lista de números separados por comas: ")
            # Convertimos la entrada en una lista de enteros
            # El strip() elimina espacios en blanco alrededor de cada número
            lis_numeros = [int(num.strip()) for num in entrada.split(",")]
            intermedio_num = intermedio(lis_numeros)
            if intermedio_num is not None:
                print(f"El número intermedio es: {intermedio_num}\n")
            else:
                print("No hay un número intermedio en la lista proporcionada.\n")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese solo números enteros separados por comas.\n")