"""crash_course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from __future__ import absolute_import
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from .views import HomePageView, SignUpView, LoginView, LogOutView, user_profile, ChangePassword

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^password_reset/', include('password_reset.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^talks/', include('talks.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^profile/$', 'crash_course.views.user_profile', name='profile'),
    url(r'^contact/$', 'talks.views.contact', name='contact'),
    url(r'^myaccounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^myaccounts/login/$', LoginView.as_view(), name='login'),
    url(r'^myaccounts/logout/$', LogOutView.as_view(), name='logout'),
    #url(r'^password-change/$', ChangePassword.as_view(), name='password_change'),
    #url(r'^accounts/password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password-change/$', 'django.contrib.auth.views.password_change', {'template_name': 'myaccounts/password_change.html'}, name='password_change'),
    
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)