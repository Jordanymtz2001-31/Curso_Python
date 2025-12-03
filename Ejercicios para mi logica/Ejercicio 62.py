def decimal_binario(n):
    # Creamos una lista vacia para almacenar los bits
    bits = []
    # Si el numero es 0, devolvemos [0]
    if n == 0:
        return 0
    # Se repetira mientras n sea mayor que 0 y se agregaran los bits a la lista
    while n > 0:
        bits.append(str(n % 2))  # Agregamos el residuo a la lista como cadena
        n //= 2  # Actualizamos n con el cociente entero
    bits.reverse()  # Invertimos la lista para obtener el orden correcto
    return bits

def binario_decimal(b):
    b = list(b)
    decimal = 0
    # Recorremos la cadena de bits de derecha a izquierda
    for i in range(len(b)):
        bit = int(b[len(b) - 1 - i])  # Obtenemos el bit actual
        decimal += bit * (2 ** i)  # Sumamos el valor del bit en su posicion
    return decimal

while True:
    try:
        print("BIENBENDOS AL PROGRAMAM DE CONVERTIDOR")
        res = input("Deseas convertir (Binario/decimal): ").lower()
        if res == "":
            print("No puedes dejar vacia la casilla")
        elif res != "binario" and res != "decimal":
            print("Respuesta no valida. Por favor ingrese 'binario' o 'decimal'.\n")
        elif res == "binario":
            n = int(input("Dame un numero para convertirlo a binario: "))
            print (f"El numero {n} a binario es {decimal_binario(n)}\n")
        elif res == "decimal":
            b = (input("Dame el numero binario a convertir: "))
            print(f"El numero {b}, en decimal es {binario_decimal(b)}\n")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese dos números enteros separados por una coma.\n")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}\n")
        
    

