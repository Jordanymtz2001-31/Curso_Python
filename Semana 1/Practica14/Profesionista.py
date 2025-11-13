from abc import ABC, abstractmethod

class Profesionista(ABC):
    def __init__(self, nombre, edad, experiencia):
        self._nombre = nombre
        self._edad = edad
        self._experiencia = experiencia

    # Metodo Concreto
    def cobrar(self, trabajo, sueldo):
        return f"Trabajo como : {trabajo} y mi sueldo es de: {sueldo}"

    #Metodo Abstracto
    @abstractmethod
    def Mensaje(self):
        pass

    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Experiencia: {self._experiencia}"
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia