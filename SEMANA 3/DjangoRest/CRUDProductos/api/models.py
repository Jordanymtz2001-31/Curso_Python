from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    class Meta:
        db_table = 'Productos'
