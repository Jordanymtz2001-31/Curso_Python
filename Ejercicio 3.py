peso_muñeca = 75
peso_payaso = 112

muñecas = int(input("Dime la cantidad de muñecas: "))
payasos = int(input("Dime la cantidad de payasos: "))

def total_peso(muñeca, payasos):
    if muñeca == 0 and payasos == 0:
        return "No hay nada que enviar"
    else:
        total_muñecas = muñeca * peso_muñeca
        total_payasos = payasos * peso_payaso

        peso_total = total_muñecas  + total_payasos

    return f"EL peso total del paquete es de {peso_total} Kg"

print (total_peso(muñecas, payasos))