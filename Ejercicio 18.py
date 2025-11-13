edad = int(input("Dame tu edad: "))
ingresos = float(input("Dime tus ingresos mensuales: "))

def tributar(edad, ingresos):
    if edad >= 16:
        if ingresos >= 1000:
            return "Tienes que tributar"
    else:
        return "No tienes que tributar"
    
print(tributar(edad, ingresos))