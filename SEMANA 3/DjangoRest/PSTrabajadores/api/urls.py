from rest_framework.routers import DefaultRouter
from .views import TrabajadorViewSet, RespaldoTrabajadorViewSet

router = DefaultRouter()
router.register('trabajadores', TrabajadorViewSet, basename='trabajadores')
router.register('resp-trabajadores', RespaldoTrabajadorViewSet, basename='resp-trabajador')

urlpatterns = router.urls