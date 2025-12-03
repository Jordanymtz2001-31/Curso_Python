"""
Escribir una función que reciba una muestra de números en una lista y 
devuelva otra lista con sus cuadrados.
"""

#Creamos la funcion para calcular los cuadrados de una lista de numeros
def lis_cuadrados(lis_numeros):
    # Usamos una lista por comprension para crear una nueva lista con los cuadrados
    # En ves de usar un ciclo for tradicional
    lis_cuad = [num ** 2 for num in lis_numeros]
    return lis_cuad

while True:
    try:
        print("\nBIENVENIDO AL PROGRAMA DE CUADRADOS DE NÚMEROS")
        res = str(input("¿Desea ingresar una lista de números? (si/no): ")).lower()
        if res == "no":
            print("Gracias por usar el programa")
            break
        elif res != "si" and res != "no":
            print("Respuesta no valida. Por favor ingrese 'si' o 'no'.\n")
        elif res == "si":
            entrada = input("Ingrese una lista de números separados por comas: ")
            # Validamos que la entrada no este vacia
            if entrada.strip() == "":
                print("La lista no puede estar vacía. Por favor, ingrese al menos un número.\n")
            elif "," not in entrada:
                print("Por favor, ingrese al menos dos números separados por comas.\n")
            else:
                # Convertimos la entrada en una lista de enteros
                # El strip() elimina espacios en blanco alrededor de cada número
                lis_numeros = [int(num.strip()) for num in entrada.split(",")]
                lis_cuad = lis_cuadrados(lis_numeros)
                print(f"La lista de cuadrados es: {lis_cuad}\n")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese solo números enteros separados por comas.\n")
