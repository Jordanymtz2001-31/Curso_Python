#Clase Profesor
from abc import abstractmethod
from Persona_Abstr import Persona


class Profesor(Persona):
    def __init__(self, matricula, nombre, edad, especialidad):
        super().__init__(matricula, nombre, edad)
        self.especialidad = especialidad

    #Metodo abstracto implementado
    def mostrar_datos(self):
        print(f"Profesor {self.nombre} Especializado en {self.especialidad}\n")