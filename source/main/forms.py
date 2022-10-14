from django import forms

from source.main.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
