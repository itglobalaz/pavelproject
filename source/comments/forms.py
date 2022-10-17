from django import forms

from source.comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
