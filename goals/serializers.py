from rest_framework import serializers

from core.serializers import UserSerializer
from goals.models import GoalCategory, Goal, GoalComment


# _______________________________________________________________
# ________________goal_category_serializers______________________
class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    """ Модель проверки объекта `Категория` является пользователь владельцем или редактором """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        fields = '__all__'
        read_only_fields = ["id", "created", "updated", "user"]

    def validate_board(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("Не разрешено в удаленном объекте")


class GoalCategorySerializer(serializers.ModelSerializer):
    """ Модель вывода объекта """
    user = UserSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        fields = '__all__'
        read_only_fields = ("id", "created", "updated", "user")


# _______________________________________________________________
# ________________goal_serializers_______________________________

class GoalCreateSerializer(serializers.ModelSerializer):
    """ Модель создания объекта `ЦЕЛЬ`. Фильтр, что объект `ЦЕЛЬ` является владельцем. """
    category = serializers.PrimaryKeyRelatedField(queryset=GoalCategory.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ["id", "created", "updated", "user"]

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("Не разрешено в удаленной категории")


class GoalSerializer(serializers.ModelSerializer):
    """ Модель объекта `ЦЕЛЬ`. """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ("id", "created", "updated", "user")

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("Не разрешено в удаленной категории")


# _______________________________________________________________
# ________________goal_cooment_serializers_______________________________
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