from __future__ import absolute_import
from django.conf.urls import include, url
from .views import TalkListView, TalkDetailView, TalkCreateView, TalkDeleteView, TalkUpdateView,\
                         TestListView, TalkListUserView, TalkArchiveView, CommentCreateView, CommentDetailView, JqueryView, AngularView

urlpatterns = [
    
    url(r'^test$', TestListView.as_view(), name='test_list'),
    url(r'^search/$', 'talks.views.search_titles', name='search'),
    url(r'^angular$', AngularView.as_view(), name='angular'),
    url(r'^jquery$', JqueryView.as_view(), name='jquery'),
    url(r'^my-talks$', TalkListUserView.as_view(), name='my_talks'),
    url(r'^$', TalkListView.as_view(), name='talk_list'),
    url(r'^(?P<pk>\d+)/$', TalkDetailView.as_view(), name='talk_detail'),
    url(r'^create/$', TalkCreateView.as_view(), name='create_list'),
    url(r'^(?P<pk>\d+)/update/$', TalkUpdateView.as_view(), name='talk_edit'),
    url(r'^(?P<pk>\d+)/delete/$', TalkDeleteView.as_view(), name='talk_delete'),
    url(r'^archive/$', TalkArchiveView.as_view(), name='talk_archive'),
    url(r'^add-comment/(?P<pk>\d+)/$', CommentCreateView.as_view(), name='comment'),
    url(r'^view-comment/(?P<pk>\d+)/$', CommentDetailView.as_view(), name='view_comment'),
    
]
