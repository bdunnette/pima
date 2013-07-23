from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Term(MPTTModel):
    doid = models.IntegerField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    definition = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    def __unicode__(self):
		return "%s: %s" % (self.doid, self.name)
