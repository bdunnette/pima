from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
from images.models import Case, Resource
from disease_ontology.models import Term
import pprint
from pyparsing import commaSeparatedList

pp = pprint.PrettyPrinter(indent=4)

def parse_js(js_file):
    vars = {}
    data = {}
    var_name = ''
    for line in js_file.readlines():
        if line.strip()[:3] == 'var':
            vars[var_name] = data
            data = {}
            var_name = line[3:].split()[0].lower()
            vars[var_name] = {}
        else:
            vals = commaSeparatedList.parseString(line)
            if len(vals) > 1:
                data[vals[0]] = vals
    return vars

class Command(BaseCommand):
    args = '<dir dir ...>'
    help = 'Imports images from the specified directories'

    def handle(self, *args, **options):
        for dir in args:
            try:
                js_file = open('/'.join([dir, 'data.js']))
                vars = parse_js(js_file)
                labs = {lab: vars[lab] for lab in vars if 'lab' in lab}
                cases = {case: vars[case] for case in vars if 'case' in case}
                for lab in labs:
                    print lab, labs[lab]
                    for case in enumerate(labs[lab]):
                        case_title = labs[lab][case[1]][1].strip(" '").title()
                        case_id = labs[lab][case[1]][2].strip()
                        print case_title
                        if case_id in cases:
                            new_case, created = Case.objects.get_or_create(title=case_title)
                            try:
                                diagnosis_term = Term.objects.get(name=case_title.lower())
                                new_case.diagnosis.add(diagnosis_term)
                            except ObjectDoesNotExist:
                                print("Diagnosis not found, skipping...")
                            #print new_case.resources
                            if created:
                                new_case.save()
                            case_info = cases[case_id]
                            for image in case_info:
                                print image, case_info[image]
                                image_filename = '/'.join([lab, image.strip("'[]")])
                                image_desc = case_info[image][1].strip(" '")
                                case_resource, resource_created = new_case.resources.get_or_create(filename=image_filename)
                                if resource_created:
                                    case_resource.description = image_desc
                                    case_resource.save()
                                    original_file_path = '/'.join([dir, lab.title(), '_images', image.strip("'[]")])
                                    print original_file_path
                                    f = open(original_file_path, 'r')
                                    i = File(f)
                                    case_resource.file.save('/'.join([lab, image]), i, save=True)
            except Exception as inst:
                print type(inst)     # the exception instance
                print inst.args      # arguments stored in .args
                print inst           # __str__ allows args to printed directly
