from django.urls import path

from source.main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/<project_slug>-<int:pk>/', views.task_detail, name='task_detail'),
    path('browse/<slug>/', views.project_detail, name='project_detail'),
]
