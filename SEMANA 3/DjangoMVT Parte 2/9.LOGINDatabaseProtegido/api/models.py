from django.db import models

# Creamos un modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    #Metodo para mostrar mensaje de si el stock es 0 que esta agotado y si es mayor que 0 que esta disponible
    def disponibilidad(self):
        if self.stock == 0:
            return "Agotado"
        else:
            return "Disponible"

    class Meta:
        db_table = 'Productos'