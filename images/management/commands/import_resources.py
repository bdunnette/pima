from django.core.management.base import BaseCommand, CommandError
from images.models import Case, Resource
import json

class Command(BaseCommand):
    args = '<dir dir ...>'
    help = 'Imports images from the specified directories'

    def handle(self, *args, **options):
	data = {}
	data2 = {}
        for dir in args:
	    var_name = ''
            try:
		js_file = open('/'.join([dir, 'data.js']))
		for line in js_file.readlines():
		    print line
	 	    if line.strip()[:3] == 'var':
			data[var_name] = data2
		        var_name = line[3:].split()[0]
			data[var_name] = {}
			data2 = {}
		    else:
			vals = line.translate(None,"{}[]\t\r\n").split(",")
			if len(vals) > 1:
			    print vals, var_name
			    data2[vals[0].strip(" '")] = vals
		for datum in data:
		    print datum, data[datum]
	    except Exception as inst:
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
