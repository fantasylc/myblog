"""myblog URL Configuration

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
from django.conf.urls import include, url,patterns
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls', namespace='blog')),
    url(r'user_auth/', include('user_auth.urls', namespace='user_auth')),
    url(r'^music/', include('music.urls', namespace='music')),
    url(r'^photo/',include('photo.urls',namespace='photo')),
    url(r'^reading/',include('reading.urls', namespace='reading'))
]

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

