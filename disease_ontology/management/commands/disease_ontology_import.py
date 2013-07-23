from django.core.management.base import BaseCommand, CommandError
from disease_ontology.models import Term
import pprint

def split_line(line):
    line_split = line.split(':', 1)
    line_type = line_split[0].strip()
    line_val = line_split[1].strip()
    return line_type, line_split

class Command(BaseCommand):
    args = '<dir dir ...>'
    help = 'Imports images from the specified directories'

    def handle(self, *args, **options):
        try:
            do_file = open('disease_ontology/HumanDO.obo')
            do_data = do_file.read().split('\n\n')
            for datum in do_data:
                datum_split = datum.split('\n')
                datum_type = datum_split[0]
                if datum_type == '[Term]':
                    for line in datum_split[1:]:
                        print split_line(line)
        except Exception as inst:
            print type(inst)     # the exception instance
            print inst.args      # arguments stored in .args
            print inst           # __str__ allows args to printed directly
