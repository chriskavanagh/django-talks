from __future__ import absolute_import
from django.shortcuts import render
#from .forms import TalksForm
from .models import TalkList
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


# Create your views here.
class TalkListView(ListView):
    model = TalkList
    template_name = 'talk_list.html'
    
    
    
class TalkDetailView(DetailView):
    model = TalkList
    template_name = 'talk_detail.html'
    
    
    
class TalkCreateView(CreateView):
    model = TalkList
    fields = ['author', 'title', 'text']
    template_name = 'talklist_form.html'
    success_url = reverse_lazy('talk_list')
    
    
    
class TalkUpdateView(UpdateView):
    model = TalkList
    template_name = 'talklist_form.html'
    fields = ['author', 'title', 'text']
    
    
    
class TalkDeleteView(DeleteView):
    model = TalkList
    template_name = 'talklist_confirm_delete.html'
    success_url = reverse_lazy('talk_list')
    
