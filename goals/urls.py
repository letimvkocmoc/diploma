from django.urls import path

from goals import views


urlpatterns = [
    path("goal_category/create", views.GoalCategoryCreateView.as_view()),
    path("goal_category/list", views.GoalCategoryListView.as_view()),
    path("goal_category/<pk>", views.GoalCategoryView.as_view()),

    path("goal_comment/create", views.CommentCreateView.as_view()),
    path("goal_comment/list", views.CommentListView.as_view()),
    path("goal_comment/<pk>", views.CommentDetailView.as_view()),
]
