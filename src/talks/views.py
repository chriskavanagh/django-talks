from __future__ import absolute_import
from django.shortcuts import render
#from .forms import TalksForm
from .models import TalkList
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class TalkListView(ListView):
    model = TalkList
    template_name = 'talk_list.html'
    
    
class TestListView(SuccessMessageMixin, ListView):
    model = TalkList
    queryset = TalkList.test_objects.all()
    template_name = 'test_detail.html'
    success_message = 'These are articles named Test'    
    
    
class TalkDetailView(DetailView):
    model = TalkList
    template_name = 'talk_detail.html'    
    
    
class TalkCreateView(SuccessMessageMixin, CreateView):
    model = TalkList
    fields = ['author', 'title', 'text']
    template_name = 'talklist_form.html'
    success_url = reverse_lazy('talk_list')
    success_message = 'A new article was created'
    
    @method_decorator(login_required)    
    def dispatch(self, *args, **kwargs):
        return super(TalkCreateView, self).dispatch(*args, **kwargs)    
    
    
class TalkUpdateView(UpdateView):
    model = TalkList
    template_name = 'talklist_form.html'
    fields = ['author', 'title', 'text']    
    
    
class TalkDeleteView(DeleteView):
    model = TalkList
    template_name = 'talklist_confirm_delete.html'
    success_url = reverse_lazy('talk_list')
    
