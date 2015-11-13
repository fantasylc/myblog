__author__ = 'liuchao'


from django.conf.urls import url, patterns

urlpatterns = patterns('blog.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^itblog/$', 'itblog', name='itblog'),
                       url(r'^itblog/article/(?P<id>\d+)/$', 'article', name='article'),
                       url(r'^comment/(?P<id>\d+)/$', 'comment', name='comment'),
                       url(r'^category/(?P<name>\w+)/$', 'category', name='category'),
                       url(r'^about/$', 'about', name='about'),
                       )
