from Productos import Productos

class Noperecedero(Productos):
    def __init__(self, nombre, precio, area):
        super().__init__(nombre, precio)
        self._area = area

    def __str__(self):
        return super().__str__() + f", Área: {self._area}"
    
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, valor):
        self._area = valor

    #sobre escribimos el metodo calcular
    def calcular(self, cantidad):
        return super().calcular(cantidad)