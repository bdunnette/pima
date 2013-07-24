from django.db import models
from django.contrib.auth.models import User
from taggit_autosuggest.managers import TaggableManager
from disease_ontology.models import Term
#from taggit.managers import TaggableManager

# Create your models here.
class Resource(models.Model):
	file = models.FileField(upload_to='resources')
	filename = models.CharField(max_length=255, unique=True, default='resource.xxx')
	description = models.TextField(null=True, blank=True)
	tags = TaggableManager(blank=True)

	def __unicode__(self):
		if self.description:
			return self.description
		else:
			return self.file.name

class Case(models.Model):
	title = models.CharField(max_length=100)
	tags = TaggableManager(blank=True)
	diagnosis = models.ManyToManyField(Term)
	resources = models.ManyToManyField(Resource)

	def __unicode__(self):
		return self.title

	
