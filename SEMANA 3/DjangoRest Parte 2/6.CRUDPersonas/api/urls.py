from api.views import PersonaViewSet
from rest_framework.routers import DefaultRouter


#Configuaracion para los metodos ViewSet
router = DefaultRouter()
router.register('personas', PersonaViewSet, basename='persona_url')

urlpatterns = router.urls


#Los metodos Personalizados ya estan configurados en la clase PersonaViewSet en los metodos buscar_ocupacion y buscar_nombre
#Se definen sus rutas 
#O Django toma el nombre de los metodos como la ruta