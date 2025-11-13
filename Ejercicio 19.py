nombre = input("Dime tu nombre: ")
sexo = input("Dime tu sexo (M/H): ").upper()

list_A = []
list_B = []

def grupos(nombre, sexo):
    if sexo == "M" and nombre.lower() < "m":
        list_A.append(nombre)
        return "Grupo A"
    elif sexo == "H" and nombre.lower() > "n":
        list_A.append(nombre)
        return "Grupo A"
    else:
        list_B.append(nombre)
        return "Grupo B"
    
print(grupos(nombre, sexo))
print("Lista del Grupo A:", list_A)
print("Lista del Grupo B:", list_B)
    