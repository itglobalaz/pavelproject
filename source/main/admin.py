from django.contrib import admin

from source.main.models import Project, Task, Membership


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'assignee', 'name', 'status', 'created_at', 'project')
    list_filter = ('status', 'project')
    list_editable = ('status',)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'project',)
