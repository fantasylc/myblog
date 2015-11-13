__author__ = 'liuchao'
from django.conf.urls import url, patterns

urlpatterns = patterns('user_auth.views',
                       url(r'^login/$', 'user_login', name='login'),
                       url(r'^logout/$', 'user_logout', name='logout'),
                       url(r'^register/$','register', name='register'),
                       )
