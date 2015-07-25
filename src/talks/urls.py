from __future__ import absolute_import
from django.conf.urls import include, url
from .views import TalkListView, TalkDetailView, TalkCreateView

urlpatterns = [
    
    url(r'^$', TalkListView.as_view(), name='talk_list'),
    url(r'^(?P<pk>\d+)/$', TalkDetailView.as_view(), name='talk_detail'),
    url(r'^create/$', TalkCreateView.as_view(), name='create_list'),
]
