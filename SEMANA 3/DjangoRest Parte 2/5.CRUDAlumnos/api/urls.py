from api.views import AlumnoViewSet
from rest_framework.routers import DefaultRouter

#Configuracion de urls para generar las rutas en automatico cuando usamos el viewset
router = DefaultRouter() 
router.register('alumnos', AlumnoViewSet, basename='alumnos_url')

#Ahora le pasamos las rutas
urlpatterns = router.urls

"""
Ruta: http://127.0.0.1:8000/alumnos/

| Método HTTP | Ruta           | Acción en el ViewSet | Descripción                      |
| ----------- | ---------------| -------------------- | -------------------------------- |
| GET         | endpoint/      | list()               | Lista todos los objetos          |
| POST        | endpoint/      | create()             | Crea un objeto                   |
| GET         | endpoint/{pk}/ | retrieve()           | Muestra un objeto específico     |
| PUT         | endpoint/{pk}/ | update()             | Actualiza un objeto              |
| PATCH       | endpoint/{pk}/ | partial_update()     | Actualiza parcialmente un objeto |
| DELETE      | endpoint/{pk}/ | destroy()            | Elimina un objeto                |

"""