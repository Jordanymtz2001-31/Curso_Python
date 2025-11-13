from django.db import models

# Create your models here.
class Trabajadores(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'TRABAJADORES'
        
class RespaldoTrabajadores(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'RESPALDO_TRABAJADORES'
