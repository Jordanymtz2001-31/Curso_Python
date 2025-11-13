num = int(input("Ingrese el numero para saber si es par o impar: "))

def par_o_impar(num):
    if num % 2 == 0:
        return f"El numero {num} es par"
    else:
        return f"El numero {num} es impar"

print(par_o_impar(num))