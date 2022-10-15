from rest_framework.permissions import BasePermission, SAFE_METHODS
# ============================================================================ #


# =============================== IS SUPER USER ============================== #

class IsSuperUser(BasePermission):
    message = 'You Must Be SuperUser'

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_superuser
        )


# ======================== IS SUPER USER OR READ ONLY ======================== #

class IsSuperUserOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and request.user.is_superuser
        )



# ========================== IS SUPER USER OR AUTHOR ========================= #

class IsSuperUserOrAuthor(BasePermission):
    message = 'You Must Be SuperUser or Author'

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and request.user.author
        )


# =================== IS SUPER USER OR AUTHOR OR READ ONLY =================== #

class IsSuperUserOrAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.author == request.user 
        )
