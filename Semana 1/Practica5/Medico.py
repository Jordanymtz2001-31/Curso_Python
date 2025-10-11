from Persona import Persona

class Medico(Persona):

    def __init__(self, nombre, edad, estado, especialidad, honorario):
        super().__init__(nombre, edad, estado)
        self._especialidad = especialidad
        self._honorario = honorario

    def __str__(self):
        return super().__str__() + f", especialidad: {self._especialidad}, Horario: {self._honorario:.2f}"
    
    @property
    def especialidad(self):
        return self._especialidad
    
    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor

    @property
    def honorario(self):
        return self._honorario
    
    @honorario.setter
    def horario(self, valor):
        self._honorario = valor    
    
    def trabajar(self, ocupacion = None, sueldo = None):
        especialidad = ocupacion or self._especialidad
        honorarios = sueldo or self._honorario

        mensaje = super().trabajar(especialidad, honorarios)
        return f"{mensaje}. Como medico brindo una atecion en el area de la salud"
