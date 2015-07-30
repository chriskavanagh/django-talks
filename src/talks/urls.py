from __future__ import absolute_import
from django.conf.urls import include, url
from .views import TalkListView, TalkDetailView, TalkCreateView, TalkDeleteView, TalkUpdateView, TestListView

urlpatterns = [
    
    url(r'^test$', TestListView.as_view(), name='test_list'),
    url(r'^$', TalkListView.as_view(), name='talk_list'),
    url(r'^(?P<pk>\d+)/$', TalkDetailView.as_view(), name='talk_detail'),
    url(r'^create/$', TalkCreateView.as_view(), name='create_list'),
    url(r'^(?P<pk>\d+)/update/$', TalkUpdateView.as_view(), name='talk_edit'),
    url(r'^(?P<pk>\d+)/delete/$', TalkDeleteView.as_view(), name='talk_delete'),
]
