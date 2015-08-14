from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class SignUpView(CreateView):
    form_class = CommentForm
    model = Comments
    template_name = 'comment.html'
    success_url = reverse_lazy('')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.talk = TalkList.objects.get(pk=self.pk)    #(pk=self.kwargs['pk'])
        
        
        
        
        
        
        
# @login_required
# def user_profile(request):
    # if request.method == 'POST':
        # form = UserProfileForm(request.POST, instance=request.user.profile)
        # if form.is_valid():
            # form.save()
            # return redirect(reverse('home'))
    # else:
        # user = request.user
        # profile = user.profile
        # form = UserProfileForm(instance=profile)
        
    # context = {'form': form}
    # return render(request, 'profile.html', context)