from rest_framework import permissions


class IsAdmin(permissions.IsAdminUser):

    def has_object_permission(self, request, view, obj):

        SAFE_METHODS = ('POST', 'PUT', 'DELETE', 'GET', 'HEAD', 'OPTIONS')

        return (
                request.method in SAFE_METHODS
        )


class ReadOnly(permissions.BasePermission):
    """
    The endpoint is read-only request.
    """

    def has_permission(self, request, view):

        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

        return (
            request.method in SAFE_METHODS
        )

