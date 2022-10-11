from django.contrib.auth.decorators import login_required
from django.shortcuts import (render, get_object_or_404)
from source.main.models import (Project, Tasks)


@login_required()
def home(request):
    return render(request, 'index.html')


@login_required()
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    tasks = Tasks.objects.filter(project=project).order_by('created_at').select_related('project')
    context = {
        'project': project,
        'tasks': tasks
    }
    return render(request, 'project_detail.html', context)


@login_required()
def task_detail(request, project_slug, pk):
    task = get_object_or_404(Tasks, project__slug=project_slug, id=pk)
    context = {
        'task': task,
    }
    return render(request, 'task_detail.html', context)
