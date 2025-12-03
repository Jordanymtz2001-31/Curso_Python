num = int(input("Ingrese el primer numero: "))
num_divisor = int(input("Ingrese el segundo numero:"))

def es_divisible(num, num_divisor):
    if num_divisor == 0:
        return "Error: No se puede dividir un numero por 0"
    else:
        resultado = num / num_divisor
        return f"\nEl resultado de la division es: {resultado}"
    

print(es_divisible(num, num_divisor))