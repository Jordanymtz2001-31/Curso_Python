from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='generar_token'), # path para obtener el token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token') # path para refrescar el token
]
