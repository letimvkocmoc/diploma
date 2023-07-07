from django.urls import path

from goals import views
from goals.views import GoalCreateView, GoalListView, GoalDetailView, CommentCreateView, CommentListView, \
    CommentDetailView

urlpatterns = [
    path('goal_category/create', views.GoalCategoryCreateView.as_view()),
    path('goal_category/list', views.GoalCategoryListView.as_view()),
    path('goal_category/<pk>', views.GoalCategoryView.as_view()),

    path('goal/create', GoalCreateView.as_view(), name='goal_create'),
    path('goal/list', GoalListView.as_view(), name='goal_list'),
    path('goal/<pk>', GoalDetailView.as_view(), name='goal_pk'),

    path('goal_comment/create', CommentCreateView.as_view(), name='comment-create'),
    path('goal_comment/list', CommentListView.as_view(), name='comment-list'),
    path('goal_comment/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
]
