from django.contrib import admin
from disease_ontology.models import Term, Synonym, CrossReference

class TermAdmin(admin.ModelAdmin):
    list_display = ('doid', 'name', 'is_obsolete')
    list_filter = ['is_obsolete']

class CrossReferenceAdmin(admin.ModelAdmin):
    list_display = ('domain', 'name')
    list_filter = ['domain']

class SynonymAdmin(admin.ModelAdmin):
    list_display = ('name', 'scope')
    list_filter = ['scope']

admin.site.register(Term, TermAdmin)
admin.site.register(Synonym, SynonymAdmin)
admin.site.register(CrossReference, CrossReferenceAdmin)
