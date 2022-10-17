from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
from django.contrib.messages.views import SuccessMessageMixin

from source.comments.forms import CommentForm
from source.comments.models import Comment
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.task_comments.order_by('-created_at')
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'etc/task_create.html'
    form_class = TaskCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, 'Поздравляем вы только что успешно добавили новый таск!')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('project_detail', kwargs={'slug': self.object.project.slug})


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'etc/task_edit.html'
    success_message = 'Задание отредактирована успешно!'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'slug': self.object.project.slug, 'pk': self.object.id})


class NewComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'etc/new_comment.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.task = get_object_or_404(Task, pk=self.kwargs['pk'], project__slug=self.kwargs['slug'])
        self.object.save()
        messages.success(self.request, 'Поздравляем вы только что успешно добавили новый коммент!')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('task_detail', kwargs={'slug': self.object.task.project.slug, 'pk': self.object.task.id})
