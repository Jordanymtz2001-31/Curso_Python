from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    cupo_maximo = models.IntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'Curso'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes', blank=True)

    class Meta:
        db_table = 'Estudiante'
