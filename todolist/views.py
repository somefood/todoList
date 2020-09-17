from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import TodoList
from .forms import TodoForm, TodoUpdateForm


class TodoIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'todolist/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_started'] = TodoList.objects.filter(username=self.request.user, is_progressed=False, is_completed=False)
        context['progressed'] = TodoList.objects.filter(username=self.request.user, is_progressed=True, is_completed=False)
        context['completed'] = TodoList.objects.filter(username=self.request.user, is_progressed=True, is_completed=True)
        return context


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = TodoList


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    form_class = TodoForm
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.request.user
        self.object.save()
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoList
    form_class = TodoUpdateForm
    success_url = reverse_lazy('todo:index')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    success_url = reverse_lazy('todo:index')