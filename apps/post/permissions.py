from rest_framework import permissions
# ============================================================================ #


# =========================== IS OWNER OR READONLY =========================== #
class IsOwnerOrReadOnly(permissions.BasePermission):
 
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user



# =========================== IS ADMIN OR READONLY =========================== #

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff