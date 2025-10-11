class Mascota:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} es un {self.tipo} \n."
    
    def hacer_ruido(self):
        return "Esta mascota esta: "