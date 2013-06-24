from django.core.management.base import BaseCommand, CommandError
from images.models import Case, Resource
import json

class Command(BaseCommand):
    args = '<dir dir ...>'
    help = 'Imports images from the specified directories'

    def handle(self, *args, **options):
        for dir in args:
            try:
	        js_file = open('/'.join([dir, 'data.js']))
		print js_file.read()
		print json.loads(js_file.read())
	    except Exception as inst:
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
