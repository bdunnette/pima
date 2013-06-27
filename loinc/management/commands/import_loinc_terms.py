from django.core.management.base import BaseCommand, CommandError
from images.models import Case, Resource
import json

class Command(BaseCommand):
    args = '<loinc_table_file>'
    help = 'Imports LOINC terms from CSV file'

    def handle(self, *args, **options):
        print args
        csv_reader = csv.reader(stream, delimiter = delimiter)

        FIELD_NAMES = ["loinc_num", "component", "property", "time_aspct", "system", "scale_typ", "method_typ", "relat_nms", "class", "source",
                       "dt_last_ch", "chng_type", "comments", "answerlist", "status", "map_to", "scope", "consumer_name", "ipcc_units", "reference",
                       "exact_cmp_sy", "molar_mass", "classtype", "formula", "species", "exmpl_answers", "acssym", "base_name", "final",
                       "naaccr_id", "code_table", "setroot", "panelelements", "survey_quest_text", "survey_quest_src", "unitsrequired", "submitted_units",
                       "relatednames2", "shortname", "order_obs", "cdisc_common_tests", "hl7_field_subfield_id", "external_copyright_notice", "example_units", "inpc_percentage",
                       "long_common_name", "hl7_v2_datatype", "hl7_v3_datatype", "curated_range_and_units", "document_section", "definition_description", "example_ucum_units"]


        for row in csv_reader:
            values = dict([(f, row[i]) for i, f in enumerate(FIELD_NAMES[:len(row)])])

            models.CodedValue.objects.create(system = codingsystem, code = values['loinc_num'],
                                             physician_value = values['component'], 
                                             consumer_value = values['consumer_name'])
