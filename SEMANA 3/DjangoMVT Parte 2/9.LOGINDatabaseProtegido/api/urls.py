from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('registro/', registro_view, name='registro'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('listar/', listar_view, name='listar'),
    path('guardar/', guardar_view, name='guardar'),
    path('editar/<int:id>/', editar_view, name='editar'),
    path('eliminar/<int:id>/', eliminar_view, name='eliminar'),
]
