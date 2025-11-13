class Banco:
    #Atrbuto estatico o de clase
    interes_anual = 0.05  # 5% de interés anual

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    #Metodo de instancia
    def calcular_interes(self):
        return self.saldo * (Banco.interes_anual)
    
#Instancias de la clase Banco
cliente1 = Banco("Banco A", 1000)
cliente2 = Banco("Banco B", 2000)

#Accedemos al atributo estatico
print(f"Interés anual del: {Banco.interes_anual}%")

#Accedemos a la variable de instancia y al metodo
print(f"Cliente 1 es: {cliente1.interes_anual}")
print(f"Cliente 2 es: {cliente2.interes_anual}")

#Calculamos el interes anual
print(f"Interés anual del cliente 1: {cliente1.calcular_interes()}")
print(f"Interés anual del cliente 2: {cliente2.calcular_interes()}")


Banco.interes_anual = 0.06 #Cambiamos el valor del atributo estatico
print(f"Nuevo interés anual del: {Banco.interes_anual}%\n")

print(f"Interés anual del cliente 1: {cliente1.calcular_interes()}")
print(f"Interés anual del cliente 2: {cliente2.calcular_interes()}")


