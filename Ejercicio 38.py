# primero preguntamos 5 veces por un numero ganador
lista_numeros = []
for i in range(5):
    numero = int(input("Ingrese un numero ganador: "))
    lista_numeros.append(numero)

    # luego mostramos los numeros ganadores de mayor a menor
    # sort() ordena de menor a mayor, por eso usamos reverse=True
lista_numeros.sort(reverse=True)
print(f"Los numeros ganadores de mayor a menor son:{lista_numeros}")



