edad = int(input("Ingrese su edad: "))

def mayor_de_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad."
    else:
        return "Eres menor de edad."
    
print(mayor_de_edad(edad))