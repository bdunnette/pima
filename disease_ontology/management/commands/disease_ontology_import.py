from django.core.management.base import BaseCommand, CommandError
from disease_ontology.models import Term
import urllib
import pprint
import re
import string

def split_line(line):
    line_split = line.split(':', 1)
    line_type = line_split[0].strip()
    line_val = line_split[1].strip()
    return line_type, line_split

def obo_parse( handle, keyid = 'name', load_obsolete=True ):
    """ Parse OBO file taking a file handler

    Code from: https://raw.github.com/INCF/neurohdf/master/neurohdf/parser/obo/oboparser.py

	Returns
	-------
	termHash : dict
	Dictionary keyed by `keyid` with the Terms and
	Typedefs
	"""
    curStanza = {}
    termHash = {}
    reStanzaStart = re.compile(r'^\[(.*)\]\s*$')
    reComment = re.compile(r'\!.*$')
    reTagLine = re.compile(r'^(\w+):\s*(.*)$')
    for line in handle:
        res = reStanzaStart.search(line)
        if res:
            if len( curStanza ):
                if load_obsolete or curStanza.get( 'is_obsolete', ['false'] )[0] == 'false':
                    termHash[ curStanza[keyid][0] ] = curStanza
            curStanza = { 'type' : [res.group(1)] }
        elif len( curStanza ):
            res = reTagLine.search( reComment.sub("", line) )
            if res:
                [tag, value] = res.groups()
                try:
                    curStanza[tag].append( value )
                except KeyError:
                    curStanza[ tag ] = [ value ]
            else:
                if len(line) > 1:
                    raise FormatError( "unparsed line: %s" % (line) )

    #get the last entry
    if len( curStanza ):
        if load_obsolete or curStanza.get( 'is_obsolete', ['false'] )[0] == 'false':
            termHash[ curStanza[keyid][0] ] = curStanza

    return termHash

class Command(BaseCommand):
    help = 'Imports images from the specified directories'

    def handle(self, *args, **options):
        try:
        	do_filename = 'disease_ontology/HumanDO.obo'
        	do_file = open(do_filename, 'w')
        	print "Downloading HumanDO file..."
        	do_svn = urllib.urlopen('http://diseaseontology.svn.sourceforge.net/svnroot/diseaseontology/trunk/HumanDO.obo')
        	do_text = do_svn.read()
        	print "Writing to file..."
        	do_file.write(do_text)
        	do_file.close()
        	do_file = open(do_filename, 'r')
        	print "Parsing data..."
        	do_data = obo_parse(do_file)
        	#print do_data
        	for datum in do_data:
        		print datum, do_data[datum]['id']
        		if 'is_a' in do_data[datum]:
        			print 'Parent:', do_data[datum]['is_a']
        	#	datum_split = datum.split('\r')
            #    #print datum_split
            #    datum_type = datum_split[0]
            #    if datum_type == '[Term]':
            #        for line in datum_split[1:]:
            #            print split_line(line)
        except Exception as inst:
            print type(inst)     # the exception instance
            print inst.args      # arguments stored in .args
            print inst           # __str__ allows args to printed directly
