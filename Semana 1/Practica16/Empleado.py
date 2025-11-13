class Empleado:
    #Variables de clase y constante
    SUELDO_BASE = 30000

    #Variable estatica
    _num_empleados = 0

    #Atributos de instancia
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        Empleado._num_empleados += 1 #Incremeta el valor con cada instancias
        

    #Metodos de estatito
    @staticmethod
    def obtener_nombre():
        return Empleado._num_empleados
    
    #Metodos de instancia
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_puesto(self):
        return self.puesto
    
    def obtener_salario(self):
        return self.salario