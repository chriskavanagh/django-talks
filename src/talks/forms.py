from __future__ import absolute_import
from django import forms
from .models import TalkList


class TalksForm(forms.ModelForm):
    class Meta:
        model = TalkList
        