"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión cada año que dura la inversión.
"""

cantidad = float(input("\nDime la cantidad a invertir: "))
interes = float(input("Dime el interes anual: "))
anos = int(input("Dime cuantos los años: "))

def calculo_capital(cantidad, interes, anos):
    for i in range(anos):
        capital = cantidad * (1 + interes) ** (i+1)
        print(f"Capital tras {i + 1} años: {capital:.2f} ")
    
print(calculo_capital(cantidad, interes, anos))