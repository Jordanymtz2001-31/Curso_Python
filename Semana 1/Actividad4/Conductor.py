class Conductor:

    def __init__(self, nombre, licencia, especialidad):
        self.nombre = nombre
        self.licencia = licencia
        self.especialidad = especialidad

    def __str__(self):
        return f"Conductor: {self.nombre}, Licencia: {self.licencia}"