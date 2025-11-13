from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSets

router = DefaultRouter()
router.register('empleados', EmpleadoViewSets, basename='empleado_url')
urlpatterns = router.urls