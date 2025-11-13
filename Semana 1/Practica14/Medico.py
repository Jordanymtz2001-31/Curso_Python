from Profesionista import Profesionista

class Medico(Profesionista):
    def __init__(self, nombre, edad, experiencia, especialidad, consultorio, costo_consulta):
        super().__init__(nombre, edad, experiencia)
        self._especialidad = especialidad
        self._consultorio = consultorio
        self._costo_consulta = costo_consulta

    #Metodo Abstracto Implementado
    def Mensaje(self):
        print("Este mensaje viene de la clase Medico")

    def __str__(self):
        return (f"{super().__str__()}, Especialidad: {self._especialidad}, "
                f"Consultorio: {self._consultorio}, Costo Consulta: {self._costo_consulta}")