from django.urls import path
from .views import PruebaAuthFaild, PruebaErrorInterno, PruebaNoAuth, PruebaNotFound, PruebaParseError, PruebaPermiso, PruebaValidation

urlpatterns = [
    path('not-found/', PruebaNotFound.as_view()),
    path('validation/', PruebaValidation.as_view()),
    path('parse-error/', PruebaParseError.as_view()),
    path('auth-faild/', PruebaAuthFaild.as_view()),
    path('permiso/', PruebaPermiso.as_view()),
    path('error/', PruebaErrorInterno.as_view()),
    path('not-auth/', PruebaNoAuth.as_view()),
]