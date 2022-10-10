from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from source.accounts.forms import UserAddForm
from source.accounts.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserAddForm
    list_display = ['email', 'username']
    model = User
