renta = float(input("Ingrese el valor de la renta anual: "))

def calcular_impuesto(renta):
    if renta < 1000:
        impuesto = renta * 0.05 
    elif renta < 2000:
        impuesto = renta * 0.15
    elif renta < 3500:
        impuesto = renta * 0.20
    elif renta < 6000:
        impuesto = renta * 0.30
    else:
        impuesto = renta * 0.45
    return impuesto

print(f"El impuesto a pagar es: {calcular_impuesto(renta)}")