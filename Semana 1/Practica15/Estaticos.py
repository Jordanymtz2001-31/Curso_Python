class Estaticos:

    #Atributos de clase estaticos
    saludo = "Hola"

    #Atributos de instancia
    def __init__(self, nombre):
        self.nombre = nombre

    #Metodo de la instancia
    #Recibe la instancia como primer parametro
    #Puede acceder a atributos de instancia y estaticos o clase
    def metodo_instancia(self):
        print(f"\nMetodo de instancia: Accede al atributo de instancia {self.nombre}")

        print(f"\nMetodo de instancia: Accede al atributo estatico {Estaticos.saludo}")


    #Metodo estatico
    #No recibe ni self ni cls
    #No puede acceder a atributos de instancia, pero si a atributos estaticos o de clase
    @staticmethod
    def metodo_estatico():
        print(f"\nMetodo estatico: No recibe self ni cls, no puede acceder a atributos de instancia")

    #Metodo de clase
    #Recibe la clase como primer parametro
    #Puede acceder a atributos de clase o estaticos a menos que explicitamente se le pase una instancia como parametro
    @classmethod
    def metodo_clase(cls):
        print(f"\nMetodo de clase: Accede al atributo estatico {cls.saludo}")

#Instancia de la clase
objeto = Estaticos("Jordany")
#Llamada al metodo de instancia
objeto.metodo_instancia()

#Llamada al metodo estatico
Estaticos.metodo_estatico()

#Llamada al metodo de clase
Estaticos.metodo_clase()