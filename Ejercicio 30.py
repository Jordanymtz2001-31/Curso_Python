num = int(input("Dame un numero entero positivo: "))

def piramide(num):
    if num < 0:
        return "El numero no puede ser negativo"
    else:
        # El primer 1 es el valor inicial
        # El segundo num + 1 es para que incluya el numero que se ingreso
        # Y el numero de iteraciones es igual a num
        for i in range(1, num + 1):
            print("*" * i)

piramide(num)