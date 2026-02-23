from django.contrib import admin

#Registramos nuestro modelo
from .models import Empleado

admin.site.register(Empleado)
