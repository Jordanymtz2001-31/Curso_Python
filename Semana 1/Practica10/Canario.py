from Mascotas import Mascota

class Canario(Mascota):

    def __init__(self, nombre, tipo, sexo):
        super().__init__(nombre, tipo)
        self.sexo = sexo

    def __str__(self):
        return super().__str__() + f"- sexo {self.sexo}\n"
    
    def hacer_ruido(self):
        return super().hacer_ruido() + "Cantando"