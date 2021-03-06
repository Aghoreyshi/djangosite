from django.conf.urls import patterns, url, include

from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'),
                       url(r'(?P<entry_id>\d+)/(?P<slug>[-\w]+)/$', views.detail, name='detail'),
                       url(r'(?P<entry_id>\d+)/$', views.detail),
                       )
