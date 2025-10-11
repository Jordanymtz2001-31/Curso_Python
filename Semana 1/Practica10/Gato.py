from Mascotas import Mascota

class Gato(Mascota):

    def __init__(self, nombre, tipo, color):
        super().__init__(nombre, tipo)
        self.color = color

    def __str__(self):
        return super().__str__() + f"- color {self.color}\n"
    
    def hacer_ruido(self):
        return super().hacer_ruido() + "Maulla"