from django.core.management.base import BaseCommand, CommandError
from disease_ontology.models import Term
import pprint
from rdflib import Graph
from rdflib.namespace import OWL

class Command(BaseCommand):
    args = '<dir dir ...>'
    help = 'Imports images from the specified directories'

    def handle(self, *args, **options):
        try:
            g = Graph()
            do_file = 'http://purl.obolibrary.org/obo/doid.owl'
            print "Downloading and parsing %s, this may take a few minutes..." % do_file
            result = g.parse(do_file, format='xml')
            for r in result:
                pprint.pprint(r)
        except Exception as inst:
            print type(inst)     # the exception instance
            print inst.args      # arguments stored in .args
            print inst           # __str__ allows args to printed directly
