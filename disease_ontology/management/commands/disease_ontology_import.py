from django.core.management.base import BaseCommand, CommandError
from disease_ontology.models import Term
import pprint

class Command(BaseCommand):
    args = '<dir dir ...>'
    help = 'Imports images from the specified directories'

    def handle(self, *args, **options):
        try:
            do_file = open('disease_ontology/HumanDO.obo')
            do_data = do_file.read().split('\n\n')
            for datum in do_data:
                datum_type = datum.split('\n')[0]
                print datum_type
        except Exception as inst:
            print type(inst)     # the exception instance
            print inst.args      # arguments stored in .args
            print inst           # __str__ allows args to printed directly
