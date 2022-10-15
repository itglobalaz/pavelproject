from django.db import models
from django.urls import reverse

from source.accounts.models import User
from source.main.constants import ProjectStatus


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Project name')
    description = models.TextField(verbose_name='Project description')
    memberships = models.ManyToManyField(User, verbose_name='Memberships', through='Membership')
    status = models.CharField(choices=ProjectStatus.choices, default=ProjectStatus.OPEN, max_length=100,
                              verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def get_project_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Task(models.Model):
    author = models.ForeignKey(User, editable=False, on_delete=models.CASCADE, verbose_name='Author', related_name='project_author',
                               null=True)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Assignee',
                                 related_name='project_assignee', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    name = models.CharField(max_length=255, verbose_name='Task name')
    description = models.TextField(verbose_name='Task description')
    status = models.CharField(choices=ProjectStatus.choices, default=ProjectStatus.OPEN, max_length=100,
                              verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name

    def get_task_url(self):
        return reverse('task_detail', kwargs={'slug': self.project.slug, 'pk': self.id})
