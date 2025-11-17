num = int(input("Dame un numero: "))

def num_primo(num):
    if num < 2:
        return "El numero no es primo"
    elif num == "":
        return "No se ingreso ningun numero"
    else:
        for i in range(2, num + 1):
            if num % i == 0 and i != num:
                return "El numero no es primo "
        return "El numero es primo"

print(num_primo(num))

while num_primo(num) != "El numero es primo":
    print(num_primo(num))
    num = int(input("Dame otro numero: "))