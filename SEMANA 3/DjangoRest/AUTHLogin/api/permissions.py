from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated: # Decimos si el usuario no esta autentificado
            return False # Retornamos False
        return request.user.empleado.rol == 'admin' # Peri si esta autentificado Retornamos True
    
class IsGerenteOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated: # Decimos si el usuario no esta autentificado
            return False # Retornamos False
        empleado = request.user.empleado
        return empleado.rol in ['gerente', 'admin']