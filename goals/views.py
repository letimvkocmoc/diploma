from django.db import transaction
from django.db.models import QuerySet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals.filters import GoalDateFilter
from goals.models import Goal, GoalCategory, GoalComment
from goals.permissions import GoalPermissions, GoalCategoryPermissions, CommentPermissions
from goals.serializers import GoalCreateSerializer, GoalSerializer, GoalCategorySerializer, \
    GoalCategoryCreateSerializer, CommentSerializer, CommentCreateSerializer


class GoalCreateView(CreateAPIView):
    """ Модель представления, которая позволяет создавать объект Goal """
    model = Goal
    serializer_class = GoalCreateSerializer
    permission_classes = [IsAuthenticated]


class GoalDetailView(RetrieveUpdateDestroyAPIView):
    """ Модель представления, которая позволяет редактировать и удалять объекты Goal. """
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated, GoalPermissions]

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user=self.request.user)

    def perform_destroy(self, instance):
        instance.status = Goal.Status.archived
        instance.save()
        return instance


class GoalListView(ListAPIView):
    """
    Модель представления, которая позволяет выводить все объекты Goal.
    Сортировать, фильтровать и искать по полям `title`, `description`
    """
    model = Goal
    permission_classes = [IsAuthenticated]
    serializer_class = GoalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]
    filterset_class = GoalDateFilter
    search_fields = ["title", "description"]
    ordering_fields = ["due_date", "priority"]
    ordering = ["priority", "due_date"]

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user=self.request.user)


class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    permission_classes = [IsAuthenticated]
    serializer_class = GoalCategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    """ Модель представления, которая позволяет просматривать все объекты Category """
    model = GoalCategory
    permission_classes = [IsAuthenticated]
    serializer_class = GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, ]
    ordering_fields = ["title", "created"]
    filterset_fields = ["board", "user"]
    ordering = ["title"]
    search_fields = ["title"]

    def get_queryset(self):
        return GoalCategory.objects.filter(board__participants__user=self.request.user, is_deleted=False)


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    """ Модель представления, которая позволяет редактировать и удалять объекты из Category """
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [IsAuthenticated, GoalCategoryPermissions]

    def get_queryset(self) -> QuerySet[GoalCategory]:
        return GoalCategory.objects.filter(board__participants__user=self.request.user).exclude(is_deleted=True)

    def perform_destroy(self, instance):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            Goal.objects.filter(category=instance).update(status=Goal.Status.archived)
        return instance


class CommentCreateView(CreateAPIView):
    """ Модель представления, которая позволяет создавать объекты Comment. """
    model = GoalComment
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    """ Модель представления, которая позволяет редактировать и удалять объекты Comment. """
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentPermissions]

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)


class CommentListView(ListAPIView):
    """
    Модель представления, которая позволяет выводить все объекты Comment.
    Так же сортирую и делает фильтрацию по полю `goal`.
    """
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["goal"]
    ordering = "-id"

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)