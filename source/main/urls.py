from django.urls import path
from source.main.views import (Home, TaskDetail, ProjectDetail, TaskCreateView, TaskUpdate, NewComment)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('browse/<slug>-<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('browse/edit/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('browse/<slug>/', ProjectDetail.as_view(), name='project_detail'),
    path('browse/<slug>/new-task/', TaskCreateView.as_view(), name='new_task'),
    path('browse/<slug>-<int:pk>/add_comment/', NewComment.as_view(), name='new_comment'),
]
