from __future__ import absolute_import
from django.views.generic import TemplateView, CreateView, FormView, RedirectView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from talks.forms import UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from talks.models import UserProfile
from talks.forms import ChangePasswordForm
from django.shortcuts import get_object_or_404


# Create your views here.
class HomePageView(SuccessMessageMixin, TemplateView):
    template_name = 'home.html'
    success_message = 'Welcome To Django 1.8 Survival Guide!'
    
    
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'myaccounts/signup.html'
    success_message = 'Welcome to Django!'
    success_url = reverse_lazy('home')
    
    
class LoginView(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'myaccounts/login.html'
    success_message = 'You Are Logged In'
    
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
        logout(request)                         # auth_logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)
        
        
        
@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
        
    context = {'form': form}
    return render(request, 'profile.html', context)
    
    
class ChangePassword(FormView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')
    template_name = 'passwordchange.html'
    
    def form_valid(self, form):
        #self.instance = form.save(commit=False)
        #user = get_object_or_404(User, username=self.request.user)        
        user = self.request.user
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        #user.password = u
        #self.instance.save()
        return super(ChangePassword, self).form_valid(form)
    
    # try u = User.objects.get(username='john')

    # def get_form_kwargs(self):
        # kwargs = super(ChangePassword, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
        # return kwargs
    
    # def form_valid(self, form):
        # self.instance = form.save(commit=False)
        # #user = get_object_or_404(User, username=self.request.user)        
        # user = self.request.user
        # password = form.cleaned_data['password']        
        # u = user.set_password(password)
        # user.password = u
        # self.instance.save()
        # return super(ChangePassword, self).form_valid(form)
        
    
    
    
    
    
    
    
# class PasswordChangeView(FormView):
    # form_class = PasswordChangeForm
    # success_url = reverse_lazy('password_change_done')
    # template_name = 'registration/password_change_form.html'
    
    # def form_valid(self, form):
        # form.save()
        # return super(LoginView, self).form_valid(form)
        