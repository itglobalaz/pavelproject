from django.contrib import admin

from source.main.models import Project, Tasks, Membership


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at')
    list_filter = ('status',)
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at')
    list_filter = ('status',)
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'project',)
