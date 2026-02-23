from django.db import models

class Empleados(models.Model):
    #Creamos una lista de duplas para los departamentos
    DEPARTAMENTOS = [
        ('TI', 'Tecnologia de la informacion'),
        ('RRHH', 'Recursos Humanos'),
        ('Logistica', 'Logistica'),
        ('Ventas', 'Ventas'),
        ('Produccion', 'Produccion')
    ]
    
    nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    depa = models.CharField(max_length=50, choices=DEPARTAMENTOS)

    #Definimos el nombre de la clase para la tabla de la base de datos
    class Meta:
        db_table = 'Empleados'