from Profesionista import Profesionista

class Abogado(Profesionista):
    def __init__(self, nombre, edad, experiencia, tipo_abogado, despacho, honorarios):
        super().__init__(nombre, edad, experiencia)
        self._tipo_abogado = tipo_abogado
        self._despacho = despacho
        self._honorarios = honorarios

    #Metodo Abstracto Implementado
    def Mensaje(self):
        print("Este mensaje viene de la clase Abogado")

    def __str__(self):
        return (f"{super().__str__()}, Tipo de Abogado: {self._tipo_abogado}, "
                f"Despacho: {self._despacho}, Honorarios: {self._honorarios}")