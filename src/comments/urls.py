from __future__ import absolute_import
from django.conf.urls import include, url




urlpatterns = [    
    
    url(r'^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
    url(r'^delete_comment/(?P<comment_id>\d+)/$', 'article.views.delete_comment'),
    
]
