from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import (render, get_object_or_404)
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

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
        return render(request, 'etc/task_form.html', context)

    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            messages.success(request, 'Поздравляем вы только что успешно добавили новый таск!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, 'etc/task_form.html', {'form': form})
