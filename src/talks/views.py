from __future__ import absolute_import
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CommentForm, ContactForm
from .models import TalkList, Comment
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.dates import ArchiveIndexView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
#from django.shortcuts import redirect
#from .forms import ContactForm


# Create your views here.

class JqueryView(TemplateView):
    template_name = 'jquery.html'
    
    
class AngularView(TemplateView):
    template_name = 'angular.html'


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
    queryset = TalkList.test_objects.all()    # .test_objects from custom manager in models.
    template_name = 'test_detail.html'    
    
    
class TalkDetailView(DetailView):
    '''view that shows individual article or list'''
    model = TalkList
    template_name = 'talk_detail.html'
    
    # def get_context_data(self, **kwargs):
        # context = super(TalkDetailView, self).get_context_data(**kwargs)
        # c = self.object.comments.all()    # use related_name instead of set_all, object is the talk instance
        # context['comments'] = c
        # return context
        
        # used object.comments.all in template instead of overriding get_context_data
        
        
class CommentDetailView(DetailView):
    '''view that shows individual article or list'''
    model = Comment
    template_name = 'comment_detail.html'
    
    
    
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
    
    
class CommentCreateView(CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'comment.html'
    success_url = reverse_lazy('talk_list')
    
    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        t = get_object_or_404(TalkList, pk=self.kwargs['pk'])
        context['talk'] = t
        return context    
    
    def form_valid(self, form):
        self.instance = form.save(commit=False)
        self.instance.talk = get_object_or_404(TalkList, pk=self.kwargs['pk'])    # or pk=self.kwargs.get('pk', None)
        self.instance.save()                                                      # redundant to save because (see below)...http://stackoverflow.com/questions/10382838/how-to-set-foreignkey-in-createview
        return super(CommentCreateView, self).form_valid(form)                    # this saves the form (again) along with instance.save()
        
    
        
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Contact Info From %s' % cd['name']
            from_email = settings.EMAIL_HOST_USER
            to_email = cd['email']
            message = cd['message']
            send_mail(subject, message, from_email, [to_email], fail_silently=False)                                  
            return redirect(reverse('home'))
    else:
        form = ContactForm()        
    context = {'form': form}
    return render(request, 'contact.html', context)
    
    
def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    talks = TalkList.objects.filter(title__contains=search_text)
    context = {'talks': talks}
    return render(request, 'ajax_search.html', context)
        
    
    
    
# rewritten using request.POST or None. puts request.POST data in or renders empty form.    
# def contact(request):
    # form = ContactForm(request.POST or None)
    # if form.is_valid():
        # cd = form.cleaned_data
        # subject = 'Contact Info From %s' % cd['name']
        # from_email = settings.EMAIL_HOST_USER
        # to_email = cd['email']
        # message = cd['message']
        # send_mail(subject, message, from_email, [to_email], fail_silently=False)                                  
        # return redirect(reverse('home'))        
    # context = {'form': form}
    # return render(request, 'contact.html', context)

    
    
    

    