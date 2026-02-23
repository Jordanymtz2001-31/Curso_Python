from api.views import CursoViewSet, EstudianteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cursos', CursoViewSet, basename='curso_url')
router.register('estudiantes', EstudianteViewSet, basename='estudiante_url')

urlpatterns = router.urls
