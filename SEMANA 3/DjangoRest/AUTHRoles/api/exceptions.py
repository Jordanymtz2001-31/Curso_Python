from rest_framework.views import exception_handler
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    #Llamamos al handler original
    response = exception_handler(exc, context)
    # exc: es el tipo de excepcion que se lanza
    # context: Informacion adicional de la excepcion.
    
    if response is not None:
        if isinstance(exc, PermissionDenied):
            response.data = {
                'error': 'No tienes permiso de realizar esta accion. Permiso denegado!'
            }
        elif isinstance(exc, NotAuthenticated):
            response.data = {
                'error': 'No enviaste las credenciales de autenticacion.'
            }
            
    return response