class Estudiante:
    def __init__(self, persona, matricula):
        self.persona = persona #Composicion
        self.matricula = matricula

    def __str__(self):
        return f"Estudiante: {self.persona},- Matricula: {self.matricula}"