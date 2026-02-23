from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.huesped_list, name='huesped_list'),
    path('guardar/', views.huesped_create, name='huesped_create'),
    path('editar/<int:id>/', views.huesped_update, name='huesped_update'),
    path('eliminar/<int:id>/', views.huesped_delete, name='huesped_delete'),
    
    path('listarR/', views.reserva_list, name='reserva_list'),
    path('crearR/', views.reserva_create, name='reserva_create'),
    path('editarR/<int:id>/', views.reserva_update, name='reserva_update'),
    path('cancelar/<int:id>/', views.reserva_cancel, name='reserva_cancel'),
    
    path('reservas/huesped/<int:huesped_id>/', views.reservas_por_huesped, name='reservas_por_huesped'),
    path('huespedes/buscar/', views.huesped_por_nombre, name='huesped_por_nombre'),
    path('reservas/fecha/', views.reservas_por_fecha, name='reservas_por_fecha'),
]
