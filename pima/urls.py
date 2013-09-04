from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pima.views.home', name='home'),
    # url(r'^pima/', include('pima.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^images/', include('images.urls')),
    url(r'^disease_ontology/', include('disease_ontology.urls')),
    url(r'^$', 'images.views.index'),
)
