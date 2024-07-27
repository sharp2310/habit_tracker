from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Проверка на владельца
    """

    message = "Только владельцы могут просматривать данный объект."

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False