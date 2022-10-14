from django.urls import path
from source.main.views import (Home, TaskDetail, ProjectDetail, TaskCreateView)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('browse/<slug>-<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('browse/<slug>/', ProjectDetail.as_view(), name='project_detail'),
    path('new-task/', TaskCreateView.as_view(), name='new_task')
]
