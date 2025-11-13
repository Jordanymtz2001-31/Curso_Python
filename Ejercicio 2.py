print("PROGRAMA PARA CALCULAR LA CANTIDAD DE AGANCIA DE UNA INVERCION\n")

interes = float(input("Dime cuanto es el interes anual:")) / 100
inversion = float(input("Dime la inversion que dara: "))
tiempo_años = int(input("Dime la cantidad de años: "))

def calculo (interes, inversion, tiempo_años):
    if interes <= 0 or inversion <= 0 or tiempo_años <= 0 :
        return "Deves de colocar los datos completos"
    else:
        calculo = inversion * (interes + 1) * tiempo_años 

        return f"El resultado de la inversion {inversion} es de {calculo}"
    
print (calculo(interes, inversion, tiempo_años))