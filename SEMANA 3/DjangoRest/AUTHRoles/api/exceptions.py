from rest_framework.views import exception_handler
from rest_framework.exceptions import PermissionDenied, NotAuthenticated, AuthenticationFailed
from rest_framework import status

# Metodo personalizado para manejar excepciones globales
def custom_exception_handler(exc, context):
    print(f"EXCEPCIÓN: {type(exc).__name__}")  # ← Ver qué llega
    #Llamamos al handler original
    response = exception_handler(exc, context)
    # exc: es el tipo de excepcion que se lanza
    # context: Informacion adicional de la excepcion.

    print(f"RESPONSE: {response}")  # ← Ver si DRF la procesa
    
    # Si la respuesta no es None, significa que DRF pudo manejar la excepcion
    if response is not None:
        if isinstance(exc, PermissionDenied): # Con isinstance verificamos el tipo de excepcion
            print(f"TIPO EXC: {type(exc)}")  # ← Debug tipo exacto
            response.data = {'error': 'No tienes permiso de realizar esta accion. Permiso denegado!'}
            response.status_code = status.HTTP_403_FORBIDDEN # Estatus 403 Credenciales validadas, pero sin permiso

        elif isinstance(exc, NotAuthenticated):
            response.data = {'error': 'No enviaste las credenciales de autenticacion.'}
            response.status_code = status.HTTP_401_UNAUTHORIZED #Estatus 401 Sin Credencial

        elif isinstance(exc, AuthenticationFailed):
            response.data = {'error': 'No enviaste las credenciales validas.'}
            response.status_code = status.HTTP_401_UNAUTHORIZED
            
    return response
