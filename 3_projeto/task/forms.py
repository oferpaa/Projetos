from django import forms
from .models import Post


class CreateTask(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'content', 'priority', 'status', 'author')