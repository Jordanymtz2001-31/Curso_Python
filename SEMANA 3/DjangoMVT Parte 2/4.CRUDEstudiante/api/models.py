from django.db import models

# Modelo para estudiantes
class Alumno(models.Model):
    ESTATUS = [
        ('Aprobado', 'Aprobado'),
        ('Reprobado', 'Reprobado')
    ]

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    apellido = models.CharField(max_length=50)
    grado = models.IntegerField()
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    estatus = models.CharField(max_length=20, choices=ESTATUS)

    #Metodo para asignarle un estatus a alumno dependiendo de su calificacion
    #Ocupamos el metodo especial save
    def save(self, *args, **kwargs):
        if self.calificacion >= 60.0:
            self.estatus = 'Aprobado'
        else:
            self.estatus = 'Reprobado'

        #Con super llamamos al metodo save de la clase padre
        super().save(*args, **kwargs) #Despues le pasamos los argumentos

    class Meta:
        db_table = 'Alumno'

