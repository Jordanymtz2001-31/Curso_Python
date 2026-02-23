from django.contrib import admin
from .models import  Empleado, Departamento

# Aqui vamos a registrar los modelos para que se muestren en el panel del administrador
# Esto para se muestren los datos en la base de datos

#Registramos el modelo Departamento
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre'] # Estos son los campos a mostrar en el administrador en la tabla
    search_fields = ['nombre'] # Estos son los campos a buscar

# Registramos el modelo Empleado
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'puesto', 'departamento', 'rol', 'get_username'] # Estos son los campos a mostrar en el administrador en la tabla
    list_filter = ['rol', 'departamento'] # Estos son los campos a filtrar
    search_fields = ['nombre', 'user__username'] # Estos son los campos a buscar

    #Metodo personalizado para mostrar el username
    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username' # Para cambiar el nombre de la columna