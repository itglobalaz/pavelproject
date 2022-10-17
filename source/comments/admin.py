from django.contrib import admin

from source.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment',)
    ordering = ['-created_at']
