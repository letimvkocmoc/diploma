from django.urls import path

from goals.views import GoalCategoryCreateView, GoalCategoryListView, GoalCategoryView, GoalListView, CommentCreateView, \
    CommentListView, CommentView, GoalCreateView, GoalView

urlpatterns = [
    path("goal_category/create", GoalCategoryCreateView.as_view()),
    path("goal_category/list", GoalCategoryListView.as_view()),
    path("goal_category/<pk>", GoalCategoryView.as_view()),

    path("goal/create", GoalCreateView.as_view()),
    path("goal/list", GoalListView.as_view()),
    path("goal/<pk>", GoalView.as_view()),

    path('goal_comment/create', CommentCreateView.as_view(), name='comment-create'),
    path('goal_comment/list', CommentListView.as_view(), name='comment-list'),
    path('goal_comment/<int:pk>', CommentView.as_view(), name='comment-detail'),
]
