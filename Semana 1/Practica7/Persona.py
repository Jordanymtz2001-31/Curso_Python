class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_inf(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
    def tipo_persona(self):
        return "Soy un tipo de persona"