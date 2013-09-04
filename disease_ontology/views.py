from disease_ontology.models import Term
from disease_ontology.serializers import TermSerializer

from rest_framework import viewsets

class TermViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows disease terms to be viewed or edited
    """
    queryset = Term.objects.all()
    serializer_class = TermSerializer
