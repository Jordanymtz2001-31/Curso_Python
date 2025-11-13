from Persona import Persona

class Informatico(Persona):

    def __init__(self, nombre, edad, estado, ocupacion, sueldo):
        super().__init__(nombre, edad, estado)
        self._ocupacion = ocupacion
        self._sueldo = sueldo

    def __str__(self):
        return super().__str__() + f", Ocupacion: {self._ocupacion}, {self._sueldo}"
    
    @property
    def ocupacion(self):
        return self._ocupacion
    
    @ocupacion.setter
    def ocupacion(self, valor):
        self._ocupacion = valor

    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, valor):
        self._sueldo = valor

    def trabajar(self, ocupacion=None, sueldo=None):
        especialidad = ocupacion or  self._ocupacion
        sueldo_v = sueldo or self._sueldo

        return super().trabajar(especialidad, sueldo_v)
