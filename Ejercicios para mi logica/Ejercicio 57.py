import math # Importamos la libreria math para usar pi

"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando 
la primera función.
"""

# Creamos las funciones para calcular el area del circulo y el volumen del cilindro
def area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def volumen_cilindro(radio, altura):
    volumen = math.pi * radio ** 2 * altura
    return volumen

while True:
    # Capturamos errores generales
    try:
        print("\nBIENVENIDO AL PROGRAMA DE CÍRCULOS Y CILINDROS")
        res = str(input("¿Desea calcular área de un círculo o volumen de un cilindro? (circulo/cilindro/no): ")).lower()
        if res == "no":
            print("Gracias por usar el programa")
            break
        # Validamos que la respuesta sea correcta
        elif res != "circulo" and res != "cilindro" and res != "no":
            print("Respuesta no válida. Por favor ingrese 'circulo', 'cilindro' o 'no'.\n")
        elif res == "circulo":
            radio = float(input("Ingrese el radio del círculo: "))
            # Validamos que el radio no sea negativo
            if radio < 0:
                print("El radio no puede ser negativo. Por favor ingrese un valor válido.\n")
            else:
                area = area_circulo(radio) # Usamos la funcion creada para calcular el area
                print(f"El área del círculo es: {area:.2f}\n")
        elif res == "cilindro":
            radio = float(input("Ingrese el radio del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            # Validamos que el radio y la altura no sean negativos
            if radio < 0 or altura < 0:
                print("El radio y la altura no pueden ser negativos. Por favor ingrese valores válidos.\n")
            else:
                volumen = volumen_cilindro(radio, altura) # Usamos la funcion creada para calcular el volumen
                print(f"El volumen del cilindro es: {volumen:.2f}\n")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números correctos para radio y altura.\n")