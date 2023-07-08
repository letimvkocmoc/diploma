from rest_framework import permissions


class GoalPermissions(permissions.BasePermission):
    """
    В коде выше мы:
        - Определили метод `has_object_permission`, который должен вернуть `True`,
          если доступ у пользователя есть, и `False` — если нет.
        - Если пользователь не авторизован, всегда возвращаем False.
        - Если метод запроса входит в SAFE_METHODS (которые не изменяют данные, например GET),
          то тогда просто проверяем, что существует участник у данной цели.
        - Если метод не входит (это значит, что мы пытаемся изменить или удалить цель), то обязательно проверяем,
          что наш текущий пользователь является создателем цели.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False


class CommentPermissions(permissions.BasePermission):
    """
    В коде выше мы:
        - Определили метод `has_object_permission`, который должен вернуть `True`,
          если доступ у пользователя есть, и `False` — если нет.
        - Если пользователь не авторизован, всегда возвращаем False.
        - Если метод запроса входит в SAFE_METHODS (которые не изменяют данные, например GET),
          то тогда просто проверяем, что существует участник у данного комментария.
        - Если метод не входит (это значит, что мы пытаемся изменить или удалить комментарий), то обязательно проверяем,
          что наш текущий пользователь является создателем комментария.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
