from django.urls import path

from source.accounts import views

urlpatterns = [
    path('', views.AddNewUser.as_view(), name='add_user')
]
