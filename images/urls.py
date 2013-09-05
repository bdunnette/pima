from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from rest_framework import routers
from images.views import *

router = routers.DefaultRouter()
router.register(r'cases', CaseViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^case/(.*)/', case, name="case"),
    url(r'^resource/(.*)/', resource, name="resource"),
    url(r'^tag/(.*)/', tag, name="tag"),
    url(r'^dx/(.*)/', diagnosis, name="diagnosis"),
    url(r'^$', index, name="index"),
)
