class Curso:

    def __init__(self, nombre):
        self._nombre = nombre
        self._estudiantes = []

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre

    @property
    def estudiantes(self):
        return self._estudiantes
    
    def agregar_estudiantes(self, new_estudiante):
        self._estudiantes.append(new_estudiante)

    def eliminar_estudiantes(self, estudiante):
        for est in self._estudiantes:
            if est == estudiante:
                self._estudiantes.remove(est)
                return True #Regresa True si se elimino
        return False
    
    def listar_estudiantes(self):
        if not self._estudiantes:
            print("No hay estudiantes inscritos en el curso.")
        else:
            for est in self._estudiantes:
                print(est.mostrar_inf())