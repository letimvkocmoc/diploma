from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals.filters import GoalDateFilter
from goals.models import GoalCategory, Goal, GoalComment
from goals.permissions import GoalPermissions, CommentPermissions
from goals.serializers import GoalCategoryCreateSerializer, GoalCategorySerializer, GoalSerializer, \
    GoalCreateSerializer, CommentCreateSerializer, CommentSerializer


class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: GoalCategoryCreateSerializer = GoalCategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    model: GoalCategory = GoalCategory
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: GoalCategorySerializer = GoalCategorySerializer
    pagination_class: LimitOffsetPagination = LimitOffsetPagination
    filter_backends: list = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    ordering_fields: list = ['title', 'created']
    ordering: list = ['title']
    search_fields: list = ['title']

    def get_queryset(self):
        return GoalCategory.objects.filter(
            user=self.request.user, is_deleted=False
        )


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model: GoalCategory = GoalCategory
    serializer_class: GoalCategorySerializer = GoalCategorySerializer
    permission_classes: list = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GoalCategory.objects.filter(user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance


class GoalCreateView(CreateAPIView):
    model: Goal = Goal
    serializer_class: GoalCreateSerializer = GoalCreateSerializer
    permission_classes: list = [IsAuthenticated]


class GoalDetailView(RetrieveUpdateDestroyAPIView):
    model: Goal = Goal
    serializer_class: GoalSerializer = GoalSerializer
    permission_classes: list = [IsAuthenticated, GoalPermissions]

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user=self.request.user)

    def perform_destroy(self, instance: Goal) -> Goal:
        instance.status = Goal.Status.archived
        instance.save()
        return instance


class GoalListView(ListAPIView):
    model: Goal = Goal
    permission_classes: list = [IsAuthenticated]
    serializer_class: GoalSerializer = GoalSerializer
    pagination_class: LimitOffsetPagination = LimitOffsetPagination
    filter_backends: list = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]
    filterset_class: GoalDateFilter = GoalDateFilter
    search_fields: list = ["title", "description"]
    ordering_fields: list = ["due_date", "priority"]
    ordering: list = ["priority", "due_date"]


class CommentCreateView(CreateAPIView):
    model: GoalComment = GoalComment
    serializer_class: CommentCreateSerializer = CommentCreateSerializer
    permission_classes: list = [IsAuthenticated]


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    model: GoalComment = GoalComment
    serializer_class: CommentSerializer = CommentSerializer
    permission_classes: list = [IsAuthenticated, CommentPermissions]


class CommentListView(ListAPIView):

    model: GoalComment = GoalComment
    serializer_class: CommentSerializer = CommentSerializer
    permission_classes: list = [IsAuthenticated]
    pagination_class: LimitOffsetPagination = LimitOffsetPagination
    filter_backends: list = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields: list = ["goal"]
    ordering: str = "-id"
