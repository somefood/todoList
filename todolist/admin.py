from django.contrib import admin
from .models import TodoList


@admin.register(TodoList)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['username', 'title', 'content', 'is_progressed', 'is_completed']
