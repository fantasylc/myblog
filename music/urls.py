from django.conf.urls import url, patterns

urlpatterns = patterns('music.views',
                       url(r'^$', 'index', name='index'),
                       )
