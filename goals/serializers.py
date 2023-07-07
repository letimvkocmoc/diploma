from rest_framework import serializers

from core.serializers import UserSerializer
from goals.models import GoalCategory, Goal


class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    user: serializers.HiddenField = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model: GoalCategory = GoalCategory
        read_only_fields: tuple = ("id", "created", "updated", "user")
        fields: list = "__all__"


class GoalCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model: GoalCategory = GoalCategory
        fields: list = '__all__'
        read_only_fields: tuple = ("id", "created", "updated", "user")


class GoalCreateSerializer(serializers.ModelSerializer):
    category: serializers.PrimaryKeyRelatedField = serializers.PrimaryKeyRelatedField(queryset=GoalCategory.objects.all())
    user: serializers.HiddenField = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model: Goal = Goal
        fields: list = '__all__'
        read_only_fields: list = ["id", "created", "updated", "user"]

    def validate_category(self, value):

        if value.is_deleted:
            raise serializers.ValidationError("Не разрешено в удаленной категории")


class GoalSerializer(serializers.ModelSerializer):
    user: UserSerializer = UserSerializer(read_only=True)

    class Meta:
        model: Goal = Goal
        fields: list = '__all__'
        read_only_fields: tuple = ("id", "created", "updated", "user")

    def validate_category(self, value):
        """
        Проверяет, что категория, связанная с целью, не удалена и пользователь является владельцем категории.
        """
        if value.is_deleted:
            raise serializers.ValidationError("Не разрешено в удаленной категории")

        if self.instance.category.board_id != value.board_id:
            raise serializers.ValidationError("Вы не создавали эту категорию")
        return value
