from django.contrib import admin
from .models import  Empleado, Departamento

# Aqui vamos a registrar los modelos para que se muestren en el panel
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre'] 
    search_fields = ['nombre']


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'puesto', 'departamento', 'rol', 'get_username']
    list_filter = ['rol', 'departamento']
    search_fields = ['nombre', 'user__username']

    #Metodo personalizado para mostrar el username
    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username' # Para cambiar el nombre de la columna