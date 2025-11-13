from rest_framework.permissions import BasePermission
# BasePermission es una clase abstracta que sirve para crear permisos personalizados.

class IsAdmin(BasePermission): #Define un permiso personalizado llamado isAdmin
    def has_permission(self, request, view): #Esta funcion decice si se permite el acceso a la vista protegida.
        # Devuelve un TRUE si el user esta autenticado y ademas su campo rol es ADMIN
        return request.user.is_authenticated and request.user.rol == 'ADMIN'
    
class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'USER'
    
class IsAdminOrUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol in ['ADMIN', 'USER']