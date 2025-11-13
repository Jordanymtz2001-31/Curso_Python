from django.urls import path
from .views import BienvenidaView, ConfigView, RegistroView, InfoView, AyudaView

urlpatterns = [
    path('bienvenida/', BienvenidaView.as_view()),
    path('config/', ConfigView.as_view()),
    path('info/', InfoView.as_view()),
    path('ayuda/', AyudaView.as_view()),
    path('registro/', RegistroView.as_view())
]