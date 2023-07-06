from rest_framework import serializers

from core.serializers import UserSerializer
from goals.models import GoalCategory, GoalComment, Goal


class GoalCreateSerializer(serializers.ModelSerializer):
    """ Модель создания объекта `ЦЕЛЬ`. Фильтр, что объект `ЦЕЛЬ` является владельцем. """
    category = serializers.PrimaryKeyRelatedField(queryset=GoalCategory.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ["id", "created", "updated", "user"]


class GoalSerializer(serializers.ModelSerializer):
    """ Модель объекта `ЦЕЛЬ`. """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ("id", "created", "updated", "user")


class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    """ Модель проверки объекта `Категория` является пользователь владельцем или редактором """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        fields = '__all__'
        read_only_fields = ["id", "created", "updated", "user"]


class GoalCategorySerializer(serializers.ModelSerializer):
    """ Модель вывода объекта """
    user = UserSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        fields = '__all__'
        read_only_fields = ("id", "created", "updated", "user")


class CommentCreateSerializer(serializers.ModelSerializer):
    """ Модель создания объекта `Комментарий` и проверки его на владельца или редактора. """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalComment
        fields = '__all__'
        read_only_fields = ("id", "created", "updated", "user")


class CommentSerializer(serializers.ModelSerializer):
    """ Модель вывода объектов `Комментарий` """
    user = UserSerializer(read_only=True)

    class Meta:
        model = GoalComment
        fields = '__all__'
        read_only_fields = ("id", "created", "updated", "user", "goal")
