from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound, ValidationError, ParseError, AuthenticationFailed, NotAuthenticated, PermissionDenied, MethodNotAllowed, APIException

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        if isinstance(exc, NotFound): #404
            response.data = {'error': 'No encontramos lo que buscas'}
        
        elif isinstance(exc, ValidationError): #400
            response.data = {'error': 'Datos invalidos', 'detalles': response.data}
            
        elif isinstance(exc, ParseError): #400
            response.data = {'error': 'Formato de datos equivocado.'}
            
        elif isinstance(exc, AuthenticationFailed): #401
            response.data = {'error': 'Las credenciales son invalidas.'}
            response.status_code = 401
        
        elif isinstance(exc, NotAuthenticated): #401
            response.data = {'error': 'Debes iniciar sesion antes.'}
            
        elif isinstance(exc, PermissionDenied): #403
            response.data = {'error': 'No tienes permiso para acceder al recurso.'}
            
        elif isinstance(exc, MethodNotAllowed): #405
            response.data = {'error': 'Te equivocaste de tipo de metodo http'}
            
        elif isinstance(exc, APIException): #500
            response.data = {'error': 'Error interno del servidor.'}
            
    return response