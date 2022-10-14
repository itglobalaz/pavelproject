from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (render, get_object_or_404)
from django.views.generic import ListView, DetailView

from source.main.models import (Project, Tasks)


class Home(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetail(LoginRequiredMixin, DetailView):
    template_name = 'project_detail.html'
    model = Project
    slug_field = 'slug'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.filter(project=self.object).order_by('created_at').select_related('project')
        return context


@login_required()
def task_detail(request, project_slug, pk):
    task = get_object_or_404(Tasks, project__slug=project_slug, id=pk)
    context = {
        'task': task,
    }
    return render(request, 'task_detail.html', context)
