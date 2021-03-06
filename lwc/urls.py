from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.signup', name='signup'),
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
)
