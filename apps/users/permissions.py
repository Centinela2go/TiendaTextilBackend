from rest_framework import permissions
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class IsInDynamicGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        allowed_groups = getattr(view, 'allowed_groups', [])
        if request.user.is_superuser:
            return True
        
        # Obtener el modelo del serializador
        serializer_class = getattr(view, 'serializer_class', None)
        permissions_extra = getattr(view, 'permissions_extra', None)
        if serializer_class:
            model_class = serializer_class.Meta.model
        else:
            model_class = None

        # Determinar la acción actual
        action = getattr(view, 'action', None)
        
        required_permission = self.get_required_permission(model_class, action) if model_class else None
        
        # Verificar si el usuario pertenece a alguno de los grupos permitidos
        user_groups = request.user.groups.values_list('name', flat=True)
        permissions_user = request.user.groups.values_list('permissions__codename', flat=True).distinct()
    
        if any(group in allowed_groups for group in user_groups): 
            # Verificar permisos adicionales
            if required_permission:
                if (required_permission in permissions_user):
                    return True
            else:
                if any(permission_extra in permissions_user for permission_extra in permissions_extra):
                    return True

        return False
    
    def get_required_permission(self, model_class, action):
        if not model_class:
            return None

        # Determinar el codename del permiso basado en la acción
        model_name = model_class._meta.model_name
        action_to_permission = {
            'list': f'view_{model_name}',
            'create': f'add_{model_name}',
            'retrieve': f'view_{model_name}',
            'update': f'change_{model_name}',
            'destroy': f'delete_{model_name}',
        }
        return action_to_permission.get(action)
