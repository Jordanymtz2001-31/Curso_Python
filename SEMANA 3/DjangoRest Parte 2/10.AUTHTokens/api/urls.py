from .views import EmpleadoViewSet
from rest_framework.routers import DefaultRouter

Router = DefaultRouter() #Instancia de la clase DefaultRouter
Router.register('empleados', EmpleadoViewSet, basename='empleados') #Registramos el endpoint empleados con la clase EmpleadoViewset

urlpatterns = Router.urls #Asignamos la variable Router a la variable urlpatterns
