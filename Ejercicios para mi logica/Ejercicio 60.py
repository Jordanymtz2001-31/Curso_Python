"""
Escribir una función que reciba una muestra de números en una lista y 
devuelva un diccionario con su media, varianza y desviación típica.
"""

# Funcion para calcular media, varianza y desviación típica de una lista
def calculos(lis_numeros):
    media = sum(lis_numeros) / len(lis_numeros)
    # La x es cada numero en la lista
    varianza = sum((n - media) ** 2 for n in lis_numeros) / len(lis_numeros)
    desviacion_tipica = varianza ** 0.5
    # Aqui regresamos en forma de diccionario
    return {"media": media, "varianza": varianza, "desviacion_tipica": desviacion_tipica}

while True:
    try:
        print("\nBIENVENIDO AL PROGRAMA DE CÁLCULOS ESTADÍSTICOS")
        res = str(input("¿Desea ingresar una lista de números? (si/no): ")).lower()
        if res == "no":
            print("Gracias por usar el programa")
            break
        elif res != "si" and res != "no":
            print("Respuesta no valida. Por favor ingrese 'si' o 'no'.\n")
        elif res == "si":
            entrada = input("Ingrese una lista de números separados por comas: ")
            if entrada.strip() == "":
                print("La lista no puede estar vacía. Por favor, ingrese al menos un número.\n")
            elif "," not in entrada:
                print("Por favor, ingrese al menos dos números separados por comas.\n")
            else:
                # Convertimos la entrada en una lista de enteros
                # El strip() elimina espacios en blanco alrededor de cada número
                lis_numeros = [int(num.strip()) for num in entrada.split(",")]
                resultados = calculos(lis_numeros)
                print(f"Resultados:\nMedia: {resultados['media']:.2f}\nVarianza: {resultados['varianza']:.2f}\nDesviación Típica: {resultados['desviacion_tipica']:.2f}\n")
    # Este except captura errores de conversion a entero
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese solo números enteros separados por comas.\n")