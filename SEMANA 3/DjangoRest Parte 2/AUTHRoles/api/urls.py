from django.urls import path
from api.views import ResgistroView, ProductoView

urlpatterns = [
    path('registrar/', ResgistroView.as_view(), name='registrar'),
    path('listar/', ProductoView.as_view(), name='listar'),
    path('guardar/', ProductoView.as_view(), name='guardar'),
    path('productos/<int:id>/', ProductoView.as_view(), name='productos_detalle'),
    path('productos/buscar_por_nombre/', ProductoView.as_view(), name='productos_buscar_nombre'),
]
