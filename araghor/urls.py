from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^araghor/', include('araghor.foo.urls')),
    url(r'^$', 'araghor.views.home', name='home'),
    url(r'^grey$', 'araghor.views.greyhome', name='greyhome'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^polls/', include('polls.urls', namespace='polls'))
)
