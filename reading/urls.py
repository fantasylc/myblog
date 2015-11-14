from django.conf.urls import url, patterns

urlpatterns = patterns('reading.views',
                       url(r'^$', 'index', name='index'),
                       )

