from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class TodoIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'todolist/index.html'