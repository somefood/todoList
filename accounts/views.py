from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import ProfileForm


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:register_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm()
        return context

    def form_valid(self, form):
        self.object = form.save()
        profile_form = ProfileForm(self.request.POST, instance=self.object.profile)
        if profile_form.is_valid():
            profile_form.save()
        return super().form_valid(form)



class UserCreateDoneView(TemplateView):
    template_name = 'registration/register_done.html'
