from django.urls import path

from source.accounts import views

urlpatterns = [
    path('', views.user_add, name='add_user')
]
