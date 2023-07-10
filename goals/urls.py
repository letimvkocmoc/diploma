from django.urls import path

from goals.views import GoalCategoryCreateView, GoalCategoryListView, GoalCategoryView, GoalCreateView, GoalListView, \
    GoalDetailView, CommentCreateView, CommentDetailView, CommentListView, BoardCreateView, BoardListView, BoardView

urlpatterns = [
    path("goal_category/create", GoalCategoryCreateView.as_view(),  name='category_create'),
    path("goal_category/list", GoalCategoryListView.as_view(),name='category_list'),
    path("goal_category/<pk>", GoalCategoryView.as_view(), name='category_pk'),

    path("goal/create", GoalCreateView.as_view(), name='goal_create'),
    path("goal/list", GoalListView.as_view(), name='goal_list'),
    path("goal/<pk>", GoalDetailView.as_view(), name='goal_pk'),

    path('goal_comment/create', CommentCreateView.as_view(), name='comment-create'),
    path('goal_comment/list', CommentListView.as_view(), name='comment-list'),
    path('goal_comment/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),

    path('board/create', BoardCreateView.as_view(), name='board_create'),
    path('board/list', BoardListView.as_view(), name='board_list'),
    path('board/<int:pk>', BoardView.as_view(), name='board_pk'),
]