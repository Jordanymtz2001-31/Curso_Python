#expresion Lambda sintaxis

#Suma con expresion lambda
suma = lambda a, b: a + b
print(suma(5, 3))  # Salida: 8

#Suma con funcion normal
def suma_normal(a, b):
    return a + b

#Cuadrado lambda
cuadrado = lambda x: x ** 2
print(cuadrado(4))  # Salida: 16

#Cuadrado funcion normal
def cuadrado_normal(x):
    return x ** 2

#Resta con expresion lambda
resta = lambda a, b: a - b
print(resta(5, 3))  # Salida: 2

#Multiplicacion con expresion lambda
multiplicacion = lambda a, b: a * b
print(multiplicacion(5, 3))  # Salida: 15

print((lambda x: x / 2)(10))  # Salida: 5.0

#Expresion lambda que multiplica una lista por un numero
lista = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, lista))
print(resultado)  # Salida: [2, 4, 6, 8, 10]

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numero)) # Filtra los números pares
print(pares)  # Salida: [2, 4, 6, 8, 10]

#Lambda funciona como una funcion normal y se puede asignar a una variable

lista = [(1, 2), (1, 8), (1, 0), (1, 4)]
lista_ordenada = sorted(lista, key=lambda x: x[1]) # Ordena la lista por el segundo elemento de cada tupla
print(lista_ordenada)  # Salida: [(1, 0), (1, 2), (1, 4), (1, 8)]

#El argumento de una expresion lambda puede ser de cualquier tipo de dato y debe de ser pequeño
#y simple, ya que si es muy grande se pierde la legibilidad del codigo
lista = [1, 2, 3, 4, 5]
lista_potencia = lambda lista: [x ** 3 for x in lista]
print(lista_potencia(lista))  # Salida: [1, 8, 27, 64, 125]