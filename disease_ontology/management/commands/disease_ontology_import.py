from django.core.management.base import BaseCommand, CommandError
from disease_ontology.models import Term, Synonym, CrossReference
import urllib
import pprint
import re
import string

def get_doid(text):
    return int(text[0].split(':')[1])

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
                print datum, do_data[datum]
                if do_data[datum]['type'][0] == 'Term':
                    new_term, term_created = Term.objects.get_or_create(doid=do_data[datum]['id'][0].split(':')[1])
                    new_term.name = datum.strip()
                    term_data = do_data[datum]
                    if 'def' in term_data:
                        new_term.definition = term_data['def']
                    if 'is_obsolete' in term_data:
                        new_term.is_obsolete = term_data['is_obsolete'][0]
                    if 'xref' in term_data:
                        for ref in term_data['xref']:
                            new_ref, created = CrossReference.objects.get_or_create(ref=ref.strip())
                            new_ref.domain = ref.split(':')[0]
                            new_ref.name = ref.split(':')[1]
                            new_ref.term.add(new_term)
                            new_ref.save()
                    if 'synonym' in term_data:
                        for syn in term_data['synonym']:
                            new_syn, created = Synonym.objects.get_or_create(name=syn)
                            new_syn.term.add(new_term)
                            new_syn.save()
                    if 'is_a' in term_data:
                        for parent in term_data['is_a']:
                            parent_term, parent_created = Term.objects.get_or_create(doid=parent.split(':')[1])
                            if new_term not in parent_term.descendants_tree():
                                parent_term.add_child(new_term)
                            parent_term.save()
                    new_term.save()
        except Exception as inst:
            print type(inst)     # the exception instance
            print inst.args      # arguments stored in .args
            print inst           # __str__ allows args to printed directly
