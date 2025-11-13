# Tabal de multiplicar
num = int(input("Dame un numero para la tabla de multiplicar: "))

def tabla_multiplicar(num):
    if num < 0:
        return "El numero no puede ser positivo"
    else:
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    
tabla_multiplicar(num)