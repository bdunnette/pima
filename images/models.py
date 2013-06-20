from django.db import models
from django.contrib.auth.models import User
from taggit_autosuggest.managers import TaggableManager
#from taggit.managers import TaggableManager

# Create your models here.
class Resource(models.Model):
	file = models.FileField(upload_to='resources')
	title = models.CharField(max_length=255, null=True, blank=True)
	tags = TaggableManager(blank=True)

	def __unicode__(self):
		if self.title:
			return self.title
		else:
			return self.file.name

class Case(models.Model):
	title = models.CharField(max_length=100)
	tags = TaggableManager(blank=True)
	resources = models.ManyToManyField(Resource)

	def __unicode__(self):
		return self.title

	
