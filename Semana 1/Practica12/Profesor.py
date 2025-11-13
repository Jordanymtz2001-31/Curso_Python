class Profesor:
    def __init__(self, persona, especialidad):
        self.persona = persona #Composicion
        self.especialidad = especialidad

    def __str__(self):
        return f"Profe. {self.persona},- Especialidad: {self.especialidad}"