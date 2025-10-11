from Transporte import Transporte

class Moto(Transporte):
    def __init__(self, tipo, tamaño, area, conductor, modelo_año):
        super().__init__(tipo, tamaño, area, conductor)
        self.modelo_año = modelo_año

    def __str__(self):
        return super().__str__() + f"\nEl  Modelo/Año: {self.modelo_año}" 

    #Hijas con sobreescritura
    def accion(self):
        return super().accion() + f" Modelo: {self.modelo_año}" 
    
    def destino(self, destino):
        return super().destino(destino) + f" Modelo: {self.modelo_año}"
