from django.db import models
from django.contrib.auth.models import User
from taggit_autosuggest.managers import TaggableManager
from disease_ontology.models import Term
import uuid

# Create your models here.
class Resource(models.Model):
	file = models.FileField(upload_to='resources')
	filename = models.CharField(max_length=255, unique=True, default=str(uuid.uuid4()))
	description = models.TextField(null=True, blank=True)
	diagnosis = models.ManyToManyField(Term, null=True, blank=True)
	tags = TaggableManager(blank=True)

	def __unicode__(self):
		if self.description:
			return self.description
		else:
			return self.file.name

class Case(models.Model):
	title = models.CharField(max_length=100)
	tags = TaggableManager(blank=True)
	diagnosis = models.ManyToManyField(Term, null=True, blank=True)
	resources = models.ManyToManyField(Resource, null=True, blank=True)

	def __unicode__(self):
		return self.title

