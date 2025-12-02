"""
Escribir una función que calcule el máximo común divisor de dos números 
y otra que calcule el mínimo común múltiplo
"""

# Funcion para calcular el máximo común divisor (MCD) de dos números
def mcd(a, b):
    # Primero nos aseguramos que a y b sean positivos
    a, b = abs(a), abs(b) # El abs() devuelve el valor absoluto
    
    while b:  # Aqui usamos el algoritmo de Euclides, se repite hasta que b sea 0
        residuo = a % b  # Calculamos el residuo
        a, b = b, residuo  # Intercambio: el nuevo 'a' es el viejo 'b', 
                            # y el nuevo 'b' es el residuo
    return a



# Función que calcula el mínimo común múltiplo de dos números
def mcm(a, b):
    if a == 0 or b == 0:
        return 0  # El MCM de cualquier número con 0 es 0
    else:
        resultado_mcd = mcd(a, b) # Aquí usamos la función mcd definida antes
        mcm_resultado = abs(a * b) // resultado_mcd # Fórmula del MCM usando el MCD
        return mcm_resultado
    
while True:
    try:
        print("\nBIENVENIDO AL PROGRAMA DE MCD Y MCM")
        res = str(input("¿Desea calcular el MCD o MCM de dos números? (si/no): ")).lower()
        if res == "no":
            print("Gracias por usar el programa")
            break
        elif res != "si" and res != "no":
            print("Respuesta no valida. Por favor ingrese 'si' o 'no'.\n")
        elif res == "si":
            entrada = input("Ingrese dos números separados por una coma: ")
            num1, num2 = map(int, entrada.split(",")) # El map() es para convertir cada parte en entero

            print(f"\nCálculo del MCD de {num1} y {num2}:")
            print(f"  Resultado: MCD = {mcd(num1, num2)}")
            print(f"\nCálculo del MCM de {num1} y {num2}:")
            print(f"\nResultado: MCM = {mcm(num1, num2)}")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese dos números enteros separados por una coma.\n")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}\n")
    
