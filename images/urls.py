from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from images.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pima.views.home', name='home'),
    # url(r'^pima/', include('pima.foo.urls')),

    url(r'^case/(.*)/', case, name="case"),
    url(r'^resource/(.*)/', resource, name="resource"),
    url(r'^tag/(.*)/', tag, name="tag"),
    url(r'^dx/(.*)/', diagnosis, name="diagnosis"),
    url(r'^$', index, name="index"),
)
