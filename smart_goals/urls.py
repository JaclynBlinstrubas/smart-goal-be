from django.urls import path
from . import views


urlpatterns = [
    path('goal/', views.GoalList.as_view(), name='goal_list'),
    path('goal/<int:pk>', views.GoalDetail.as_view(), name='goal_detail'),
]