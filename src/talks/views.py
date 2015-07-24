from __future__ import absolute_import
from django.shortcuts import render
from .forms import TalksForm
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
    form_class = TalksForm
    
