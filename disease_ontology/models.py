from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_dag.models import *

# Create your models here.
class Term(node_factory('TermRelationship')):
    doid = models.IntegerField(max_length=10)
    name = models.CharField(max_length=255)
    definition = models.TextField(null=True, blank=True)
    is_obsolete = models.BooleanField()
    
    def __unicode__(self):
		return "%s: %s" % (self.doid, self.name)


class CrossReference(models.Model):
    ref = models.CharField(max_length=128, primary_key=True, unique=True)
    term = models.ManyToManyField(Term, null=True, blank=True)
    domain = models.CharField(max_length=60, default='NA')
    name = models.CharField(max_length=60, default='0000')

    def __unicode__(self):
		return self.ref


class Synonym(models.Model):
    SCOPE_CHOICES = (
        ('EXACT', 'Exact'),
        ('RELATED', 'Related'),
        ('BROAD', 'Broad'), 
        ('NARROW', 'Narrow'), 
        
    )
    term = models.ManyToManyField(Term)
    name = models.CharField(max_length=255, unique=True)
    scope = models.CharField(max_length=10, choices=SCOPE_CHOICES, default='EXACT')
    cross_reference = models.ManyToManyField(CrossReference, blank=True, null=True)

    def __unicode__(self):
		return self.name

    
class TermRelationship(edge_factory('Term', concrete = False)):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
		return "%s:%s" % (self.parent, self.child)
