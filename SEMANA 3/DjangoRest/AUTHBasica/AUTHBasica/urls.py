from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registrar_usuario), #Ruta libre
    path('bienvenida/', views.bienvenida), #Ruta libre
    path('informacion/', views.informacion),  #Ruta protegida
    path('noticias/', views.noticias) #Ruta protegida
]
