contraseña = "dany123A"

cont = input("Dame la contraseña correcta: ")

def login(cont):
    if cont == contraseña.lower(): #Con lower() se ignora las mayusculas y minusculas
        return "Acceso concedido."
    else:
        return "Acceso denegado."

print(login(cont))