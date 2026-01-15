from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSets, EmpleadoViewSets

router = DefaultRouter()
router.register('departamentos', DepartamentoViewSets, basename= 'departamentos')
router.register('empleados', EmpleadoViewSets, basename= 'empleados')

urlpatterns = [
    path('', include(router.urls)),
]