#Herencia jerarquica

class Persona:
    def __init__(self, nombre, edad, estado):
        self._nombre = nombre
        self._edad = edad
        self._estado = estado

    def __str__(self):
        return f"Persona: {self._nombre}, {self._edad}, {self._estado}"
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, valor):
        self._estado = valor

    def trabajar(self, ocupacion, sueldo):
        return f"Yo trabajo de {ocupacion} y gano {sueldo: .2f}"