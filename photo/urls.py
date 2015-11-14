from django.conf.urls import url, patterns

urlpatterns = patterns('photo.views',
                       url(r'^$', 'index', name='index'),
                       )

