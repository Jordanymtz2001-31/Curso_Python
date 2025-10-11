class Calculadora:

    PI = 3.1416

    #Metodo estatico
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def restar(a, b):   
        return a - b
    
#Accedemos a la constante y al metodo estatico sin crear un objeto
print("Valor de PI:", Calculadora.PI)

#Usamos los metodos estaticos
print("Suma:", Calculadora.sumar(5, 3))
print("Resta:", Calculadora.restar(10, 4))
