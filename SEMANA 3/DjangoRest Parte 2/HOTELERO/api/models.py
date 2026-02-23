# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class Huesped(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'HUESPEDES'

class Reserva(models.Model):
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    habitacion = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    huesped = models.ForeignKey(Huesped, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'RESERVAS'

    # funcion para validar las fechas
    def clean(self):
        super().clean()  # Llama validaciones de campos individuales
        if self.fecha_salida <= self.fecha_entrada:
            raise ValidationError({
                'fecha_salida': 'La fecha de salida debe ser posterior a la fecha de entrada.'
            })
