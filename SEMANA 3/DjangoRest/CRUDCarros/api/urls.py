from django.urls import path
from .views import CarroViewSet
from rest_framework.routers import DefaultRouter

#DefaultRuter es un clase de DRF que generara todas las rutas de forma automatica
router = DefaultRouter()
#Registramos la clase CarroViewSet en el router con el endpoint "carros" y el nombre base "carro_url"
router.register('carros', CarroViewSet, basename='carro_url')

urlpatterns = router.urls

#Ruta: http://localhost:8000/carros/

""" 
| Método HTTP | Ruta         | Acción en el ViewSet | Descripción                      |
| ----------- | -------------| -------------------- | -------------------------------- |
| GET         | carros/      | list()               | Lista todos los objetos          |
| POST        | carros/      | create()             | Crea un objeto                   |
| GET         | carros/{pk}/ | retrieve()           | Muestra un objeto específico     |
| PUT         | carros/{pk}/ | update()             | Actualiza un objeto              |
| PATCH       | carros/{pk}/ | partial_update()     | Actualiza parcialmente un objeto |
| DELETE      | carros/{pk}/ | destroy()            | Elimina un objeto                |
"""