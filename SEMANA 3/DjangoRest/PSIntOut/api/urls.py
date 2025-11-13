from rest_framework.routers import DefaultRouter
from .views import PostresViewSets

router = DefaultRouter()
router.register('postres', PostresViewSets, basename='postres')
urlpatterns = router.urls