from django.db import models
from django.urls import reverse

from source.accounts.models import User


class Project(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Archive', 'Archive'),
    )
    name = models.CharField(max_length=255, verbose_name='Project name')
    description = models.TextField(verbose_name='Project description')
    memberships = models.ManyToManyField(User, verbose_name='Memberships', through='Membership')
    status = models.CharField(choices=STATUS, default='Active', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def get_project_url(self):
        return reverse('project_detail', args=[self.slug])


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Tasks(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Archive', 'Archive'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    name = models.CharField(max_length=255, verbose_name='Task name')
    description = models.TextField(verbose_name='Task description')
    memberships = models.ManyToManyField(User, verbose_name='Memberships')
    status = models.CharField(choices=STATUS, default='Active', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name

    def get_task_url(self):
        return reverse('task_detail', kwargs={'project_slug': self.project.slug, 'pk': self.id})
