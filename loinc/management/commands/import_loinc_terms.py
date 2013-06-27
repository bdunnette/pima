from django.core.management.base import BaseCommand, CommandError
from images.models import Case, Resource
import json

class Command(BaseCommand):
    args = '<loinc_table_file>'
    help = 'Imports LOINC terms from CSV file'

    def handle(self, *args, **options):
        print args
