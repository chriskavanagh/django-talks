from __future__ import absolute_import
from django.views.generic import TemplateView, CreateView, FormView, RedirectView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'accounts/signup.html'
    
    
class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)
            
            
class LogOutView(RedirectView):
    url = reverse_lazy('home')
    
    @method_decorator(login_required)    
    def dispatch(self, *args, **kwargs):
        return super(LogOutView, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)


    