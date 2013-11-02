from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'araghor.views.home', name='home'),
    url(r'grey$', 'araghor.views.grey', name='grey'),
    url(r'cv$', 'araghor.views.cv', name='cv'),

    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    url(r'^admin/', include(admin.site.urls)),
)
