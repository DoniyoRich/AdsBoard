from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Проверка пользователя на принадлежность к группе модераторов.
    """

    def has_permission(self, request, view):
        return request.user.is_staff == True or request.user.is_superuser == True


class IsOwner(permissions.BasePermission):
    """
    Проверка объекта на принадлежность пользователю.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
