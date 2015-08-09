from __future__ import absolute_import
from django import forms
from .models import TalkList, UserProfile


class TalksForm(forms.ModelForm):
    class Meta:
        model = TalkList
        fields = ('author', 'title', 'text')
        
        
        
class UserProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ('gender', 'location')
        