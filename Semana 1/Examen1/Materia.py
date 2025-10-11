#Clase Materia

class Materia:
    def __init__(self, nombre, profesor, lista_estudiantes=None):
        self.nombre = nombre
        self.profesor = profesor
        self.lista_estudiantes = lista_estudiantes if lista_estudiantes is not None else []

    def agregar_estudiante(self, estudiante):
        #Validamos
        if estudiante not in self.lista_estudiantes:
            self.lista_estudiantes.append(estudiante)
            return True
        return False

    def estudiantes_aprobados(self, calificacion_minima=60):
        estudiantes_aprobados = []                   # Meto los estudiantes que aprueban en una lista
        for estudiante in self.lista_estudiantes:    # Recorro la lista de estudiantes
            promedio = estudiante.calcular_promedio()# Calculo el promedio de cada estudiante
            if promedio >= calificacion_minima:      # Si el promedio es mayor o igual a la calificacion minima
                estudiantes_aprobados.append(estudiante) # Agrego el estudiante a la lista de aprobados
        return estudiantes_aprobados                    # Retorno la lista de estudiantes aprobados
    