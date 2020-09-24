from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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


def todo_change_status(request):
    if request.method == "POST":
        todo_item = get_object_or_404(TodoList, pk=request.POST.get('pk'))
        status = request.POST.get('status')
        if status == "ns":
            todo_item.is_progressed = False
            todo_item.is_completed = False
        elif status == "pg":
            todo_item.is_progressed = True
            todo_item.is_completed = False
        else:
            todo_item.is_progressed = True
            todo_item.is_completed = True
        todo_item.save()
    return JsonResponse({'status_change': 'success'})


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = TodoList


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    form_class = TodoForm
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.request.user
        if self.kwargs['status'] == "progressed":
            self.object.is_progressed = True
        elif self.kwargs['status'] == "completed":
            self.object.is_progressed = True
            self.object.is_completed = True
        else:
            self.object.is_progressed = False
            self.object.is_completed = False
        self.object.save()
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoList
    form_class = TodoUpdateForm
    success_url = reverse_lazy('todo:index')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    success_url = reverse_lazy('todo:index')