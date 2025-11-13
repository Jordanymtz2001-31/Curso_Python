from Mascotas import Mascota

class Perro(Mascota):

    def __init__(self, nombre, tipo, raza):
        super().__init__(nombre, tipo)
        self.raza = raza

    def __str__(self):
        return super().__str__() + f"Raza: {self.raza} \n"
    
    #POLIMORFISMO Dinamico o de sobreescritura
    def hacer_ruido(self):
        return super().hacer_ruido() + "Ladrando"