import math

class Fraccion:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    #Metodo para simplificar la fraccion
    def simplificar(self):
        mcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def demostrar(self):
        print(f"{self.numerador}/{self.denominador}")


    #Sobre carga de operadores +
    def __add__(self, otra_fraccion):
        #SUMA de la forma de cruz
        #Calculamos el numerador
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        #Calculamos el denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        #Instanciamos la nueva fraccion
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        #Simplificamos la fraccion resultado
        resultado.simplificar()
        #Retornamos el resultado
        return resultado
    
#Instnaciamos dos fracciones
frac1 = Fraccion(1, 2)
frac2 = Fraccion(3, 4)

frac3 = frac1 + frac2

frac3.demostrar()  # Deberia mostrar 5/4