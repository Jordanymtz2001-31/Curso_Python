from Empleado import Empleado
from Empresa import Empresa

if __name__ == "__main__":

    #Creamos las instancias de empleados
    #Crear empleados
    emp1 = Empleado("Jordany", "Desarrollador", 50000)
    emp2 = Empleado("Ana", "Diseñadora", 45000)
    emp3 = Empleado("Luis", "Gerente", 70000)

    #Añadir empleados a la empresa
    Empresa.añadir_empleado(emp1)
    Empresa.añadir_empleado(emp2)
    Empresa.añadir_empleado(emp3)

    #Mostrar informacion de empleados (ESTATICOS)
    print(f"Empresa {Empresa.NOMBRE_EMPRESA}") #Constante
    print(f"Direccion {Empresa.direccion_empresa}") #Variable Estatica
    print(f"Total Empleados: {Empresa.obtener_total_empleados()}")#Metodo estatito

    #INFORMACION DE LOS EMPLADOS
    print("\n--EMPLEADOS--")
    print(f"Empleado 1: {emp1.obtener_nombre()}, Puesto: {emp1.obtener_puesto()}, Salario: {emp1.obtener_salario()}")
    print(f"Empleado 2: {emp2.obtener_nombre()}, Puesto: {emp2.obtener_puesto()}, Salario: {emp2.obtener_salario()}")
    print(f"Empleado 3: {emp3.obtener_nombre()}, Puesto: {emp3.obtener_puesto()}, Salario: {emp3.obtener_salario()}")

    #Mostrar numero total de empleados usando metodo estatico de la clase Empleado
    print(f"Número total de empleados  {Empresa.obtener_total_empleados()}")