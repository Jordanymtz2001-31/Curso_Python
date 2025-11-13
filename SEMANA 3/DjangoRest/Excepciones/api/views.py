from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ValidationError, ParseError, AuthenticationFailed, NotAuthenticated, PermissionDenied, APIException

# Create your views here.
class PruebaNotFound(APIView):
    def get(self, request):
        raise NotFound()
    
class PruebaValidation(APIView):
    def get(self, request):
        raise ValidationError({'password': 'Falta el valor del password'})
    
class PruebaParseError(APIView):
    def get(self, request):
        raise ParseError()
    
class PruebaAuthFaild(APIView):
    def get(self, request):
        raise AuthenticationFailed()
    
class PruebaNoAuth(APIView):
    def get(self, request):
        raise NotAuthenticated()
    
class PruebaPermiso(APIView):
    def get(self, request):
        raise PermissionDenied()
    
class PruebaErrorInterno(APIView):
    def get(self, request):
        raise APIException()
