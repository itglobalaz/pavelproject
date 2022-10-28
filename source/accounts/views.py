from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from source.accounts.forms import UserAddForm
from source.accounts.models import User


class AddNewUser(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserAddForm
    template_name = 'registration/registration.html'
    success_message = 'Вы добавили нового пользователя'

    def get_success_url(self):
        return reverse('add_user')
