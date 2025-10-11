class Empresa:
    #Constante
    NOMBRE_EMPRESA = "ENUCOM"

    #Variables estaticos
    direccion_empresa = "Av. Juarez 2915 int 101"
    total_empleado = 0

    @staticmethod
    def añadir_empleado (empleado):
        Empresa.total_empleado += 1

    @staticmethod
    def obtener_total_empleados():
        return Empresa.total_empleado