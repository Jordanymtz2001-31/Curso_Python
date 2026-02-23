from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('registro/', registro_view, name='registro'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
