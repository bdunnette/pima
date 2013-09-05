from images.models import Case, Resource
from rest_framework import serializers

class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
