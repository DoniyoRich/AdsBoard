from rest_framework import permissions

from config.constants import USER_ROLE


class IsAdmin(permissions.BasePermission):
    """
    Проверка пользователя на принадлежность к группе модераторов.
    """

    def has_permission(self, request, view):
        return request.user.role == USER_ROLE[0][1]


class IsOwner(permissions.BasePermission):
    """
    Проверка объекта на принадлежность пользователю.
    """

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
