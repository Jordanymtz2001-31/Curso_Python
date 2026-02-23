from django.db import models

# Creamos nuestros modelos
class Instructores(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    curso = models.CharField(max_length=50)
    experiens = models.IntegerField()

    #Metodo str
    def __str__(self):
        return f"Instructor: {self.name} - Edad: {self.age} - Curso: {self.curso} - Experiencia: {self.experiens}"