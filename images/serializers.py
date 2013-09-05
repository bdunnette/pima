from images.models import Case, Resource
from rest_framework import serializers

class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = ('url', 'title', 'diagnosis', 'resources')

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ('url', 'description', 'diagnosis', 'file')
