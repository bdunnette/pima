from disease_ontology.models import Term
from rest_framework import serializers


class TermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Term
