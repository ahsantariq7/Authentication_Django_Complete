from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import SignUpForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import my_store



class OnlyProfileView(TemplateView):
    template_name='registration/profile.html'


class ProfileView(UpdateView):
    model=User
    fields = ['username', 'first_name','last_name', 'email',]
    template_name='registration/profile.html'
    success_url = reverse_lazy('home')


class PasswordChangedView(TemplateView):
    template_name='registration/success_password_change.html'
    
# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')


class AuthListView(LoginRequiredMixin,ListView):
    model=User
    template_name='home.html'
    context_object_name='ahsan'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myname"] = 'My name is'
        return context
   
    
class DeleteProfileView(DeleteView):
    model=User
    template_name='registration/delete.html'
    success_url = reverse_lazy('home')


class ShowList(LoginRequiredMixin,ListView):
    model=my_store
    template_name='home.html'
    context_object_name='ahsan'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ahs"] = 'Helo'
        return context