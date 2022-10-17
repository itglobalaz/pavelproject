from django.db import models

from source.accounts.models import User
from source.main.models import Task


class Comment(models.Model):
    task = models.ForeignKey(Task, editable=False, verbose_name='Task', related_name='task_comments',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(User, editable=False, verbose_name='Author', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
