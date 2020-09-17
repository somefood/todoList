from django import forms
from .models import TodoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'content']


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'content', 'is_progressed', 'is_completed']