from abc import ABS, abstractmethod


class Persona(ABS):

    def __init__(self, matricula, nombre, edad):
        self._matricula = matricula
        self._nombre = nombre
        self._edad = edad

    #Metodo abstractos
    @abstractmethod
    def mostrar_datos(self):
        pass

    #Metodo estatico
    @staticmethod
    def validar_edad(edad):
        return isinstance(edad, int) and 0 < edad <= 25 #Isinstance verifica si es del tipo int
    
    @staticmethod
    def validar_nombre(nombre):
        return isinstance(nombre, str) and len(nombre) > 0 #Isinstance verifica si es del tipo str
    
    @staticmethod
    def validar_matricula(matricula):
        return isinstance(matricula, str) and matricula.isalnum() and len(matricula) #el isalnum sirve

    #Getters y Setters
    @property
    def matricula(self):
        return self._matricula
    
    def set_matricula(self, matricula):
        self._matricula = matricula

    @property
    def nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        self._edad = edad