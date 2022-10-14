from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (render, get_object_or_404)
from django.views.generic import ListView, DetailView

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
        context['tasks'] = Task.objects.filter(project=self.object).order_by('created_at').select_related('project')
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    template_name = 'task_detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task)
        return context
