from django.contrib import messages
from django.shortcuts import render

from source.accounts.forms import UserAddForm


def user_add(request):
    form = UserAddForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем вы только что успешно добавили нового пользователя!')
        else:
            messages.warning(request, 'Что то пошло не так!')
    return render(request, 'registration/registration.html', {'form': form})
