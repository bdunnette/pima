from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_dag.models import *
from categories.models import CategoryBase

class Term(CategoryBase):
    class Meta:
        verbose_name_plural = 'terms'
