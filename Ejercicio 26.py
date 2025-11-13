
num = int(input("Dame un numero: "))

def impar(num):
    if num < 0:
        return "El numero no puede ser negativo"
    elif num == "":
        return "No se ingreso ningun numero"
    else:
        mensaje = []
        for impar in range(num + 1):
            if impar % 2 != 0:
                mensaje.append(impar)

    return mensaje

print(impar(num))