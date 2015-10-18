from __future__ import absolute_import
from django import forms
from .models import TalkList, UserProfile, Comment
from django.contrib.auth.models import User


class TalksForm(forms.ModelForm):
    class Meta:
        model = TalkList
        fields = ('author', 'title', 'text')
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')        
        
        
class UserProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ('gender', 'location')
        
        
class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)
        
        
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)        