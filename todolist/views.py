from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import TodoList


class TodoIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'todolist/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_started'] = TodoList.objects.filter(username=self.request.user, is_progressed=False, is_completed=False)
        context['progressed'] = TodoList.objects.filter(username=self.request.user, is_progressed=True, is_completed=False)
        context['completed'] = TodoList.objects.filter(username=self.request.user, is_progressed=True, is_completed=True)
        return context