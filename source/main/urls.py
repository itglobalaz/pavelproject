from django.urls import path
from source.main.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('browse/<project_slug>-<int:pk>/', task_detail, name='task_detail'),
    path('browse/<slug>/', ProjectDetail.as_view(), name='project_detail'),
]
