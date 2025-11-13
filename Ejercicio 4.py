print("PROGRAMA DE DESCUENTOS DE BARRAS DE CHOCOLATE\n")

panes = int(input("Cuantos panes quieres: "))
sabor = str(input("De que sabo quieres: "))
precio = 4

def calculo(panes, sabor):
    if panes <= 0:
        return "No te puedo dar menos de 0 panes"
    elif panes > 0 and sabor == "fresa":
        total = panes * (precio * 0.7)
    else:
        total = panes * precio
    return total


print (calculo(panes, sabor))

        
