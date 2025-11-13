#Herencia multinivel: una clase hija que hereda de una clase padre que a su vez hereda de otra clase padre

class Vehiculo: #Clase abuelo

    def mover(self):
        return "El vehiculo se esta moviendo"
    
class Coche(Vehiculo): #Clase padre

    def acelerar(self):
        return super().mover() + " y el coche esta acelerando"

class Deportivo(Coche): #Clase hijo

    def turbo(self):
        return super().acelerar() + " y el coche deportivo tiene turbo"
    
#Instanciamos un objeto de la clase Deportivo
#Entonces puede usar los metodos de las clases padre y abuelo
mi_deportivo = Deportivo()
print(mi_deportivo.mover()) #Metodo de la clase abuelo
print(mi_deportivo.acelerar()) #Metodo de la clase padre
print(mi_deportivo.turbo()) #Metodo de la clase hijo