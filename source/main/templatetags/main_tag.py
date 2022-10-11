from django import template

from source.main.models import Project, Tasks

register = template.Library()


@register.simple_tag()
def get_projects():
    return Project.objects.order_by('created_at')

