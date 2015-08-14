from __future__ import absolute_import
from django.shortcuts import render
#from .forms import TalksForm
from .models import TalkList
from django.core.urlresolvers import reverse_lazy
from django.views.generic.dates import ArchiveIndexView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class TalkListView(ListView):
    '''view that displays all lists'''
    model = TalkList
    template_name = 'talk_list.html'
    
    
class TalkListUserView(ListView):
    '''user specific talk list'''
    model = TalkList
    template_name = 'talk_user.html' 
    
    @method_decorator(login_required)    
    def dispatch(self, *args, **kwargs):
        return super(TalkListUserView, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        return self.request.user.lists.all()
    
    
class TestListView(ListView):
    '''view that shows lists w/title=test. TestTalkManager'''
    model = TalkList
    queryset = TalkList.test_objects.all()
    template_name = 'test_detail.html'    
    
    
class TalkDetailView(DetailView):
    '''view that shows individual article or list'''
    model = TalkList
    template_name = 'talk_detail.html'    
    
    
class TalkCreateView(SuccessMessageMixin, CreateView):
    '''view that creates articles or lists'''
    model = TalkList
    fields = ['author', 'title', 'text']
    template_name = 'talklist_form.html'
    success_url = reverse_lazy('talk_list')
    success_message = 'A new article was created'
    
    @method_decorator(login_required)    
    def dispatch(self, *args, **kwargs):
        return super(TalkCreateView, self).dispatch(*args, **kwargs)    
    
    
class TalkUpdateView(UpdateView):
    '''view for editing or updating list'''
    model = TalkList
    template_name = 'talklist_form.html'
    fields = ['author', 'title', 'text']    
    
    
class TalkDeleteView(DeleteView):
    '''view for deleting lists'''
    model = TalkList
    template_name = 'talklist_confirm_delete.html'
    success_url = reverse_lazy('talk_list')
    
    
class TalkArchiveView(ArchiveIndexView):
'''view that shows archive by date'''
    model = TalkList
    template_name = 'talklist_archive.html'
    date_field = 'timestamp'
    
    
