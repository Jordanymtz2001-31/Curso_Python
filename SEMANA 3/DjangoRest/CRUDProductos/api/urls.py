from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_y_guardar, name='create'),
    path('<int:id>/', views.detalles, name='detail')
]