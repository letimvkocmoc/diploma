from django.urls import path

from goals import views
from goals.views import GoalCreateView, GoalListView, GoalDetailView

urlpatterns = [
    path('goal_category/create', views.GoalCategoryCreateView.as_view()),
    path('goal_category/list', views.GoalCategoryListView.as_view()),
    path('goal_category/<pk>', views.GoalCategoryView.as_view()),

    path('goal/create', GoalCreateView.as_view(), name='goal_create'),
    path('goal/list', GoalListView.as_view(), name='goal_list'),
    path('goal/<pk>', GoalDetailView.as_view(), name='goal_pk'),
]
