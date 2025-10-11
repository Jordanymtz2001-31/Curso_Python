from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    # Sobrescribimos el método mostrar_inf
    #Y juntamos la informacion de la clase padre con la de la clase hija
    def mostrar_inf(self):
        return super().mostrar_inf() + f" y mi matrícula es {self.matricula}."
    
    def tipo_persona(self):
        return super().tipo_persona() + " -> estudiante"