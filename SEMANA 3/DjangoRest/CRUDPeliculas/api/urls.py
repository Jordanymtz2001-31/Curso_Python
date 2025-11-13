from rest_framework.routers import DefaultRouter
from .views import PeliculaViewSets

router = DefaultRouter()
router.register('peliculas', PeliculaViewSets, basename='peliculas_url')
urlpatterns = router.urls