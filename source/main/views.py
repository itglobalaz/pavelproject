from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import (render)
from django.urls import reverse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
from django.contrib.messages.views import SuccessMessageMixin

from source.main.forms import TaskCreateForm
from source.main.models import (Project, Task)


class Home(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetail(LoginRequiredMixin, DetailView):
    template_name = 'project_detail.html'
    model = Project
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(project=self.object).order_by('-created_at').select_related('project')
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    template_name = 'task_detail.html'
    model = Task


class TaskCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': TaskCreateForm()}
        return render(request, 'etc/task_create.html', context)

    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Поздравляем вы только что успешно добавили новый таск!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, 'etc/task_create.html', {'form': form})


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'etc/task_edit.html'
    success_message = 'Задание отредактирована успешно!'

    def get_success_url(self):
        return reverse('task_update', kwargs={'pk': self.object.id})
