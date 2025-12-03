lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lis.reverse()

def separar_coma(lista):
    resultado = ''
    for numero in lista:
        resultado += str(numero) + ', '
    return resultado  # Eliminar la última coma y espacio

print(separar_coma(lis))