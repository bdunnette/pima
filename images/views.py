from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from images.models import Case, Resource
from disease_ontology.models import Term
from taggit.models import Tag, TaggedItem

def index(request):
	case_list = Case.objects.order_by('title')
	tag_list = Tag.objects.all()
	return render(request, 'images/index.html', {'case_list': case_list, 'tag_list': tag_list})

def case(request, case_id):
	case = get_object_or_404(Case, id=case_id)
	resources = Resource.objects.filter(case=case.id)
	diagnoses = [[[(parent.name, parent.id) for parent in diagnosis.ancestors_tree()], (diagnosis.name, diagnosis.id)] for diagnosis in case.diagnosis.all()]
	return render(request, 'images/case.html', {'case': case, 'resources': resources, 'diagnoses': diagnoses})

def resource(request, resource_id):
	resource = get_object_or_404(Resource, id=resource_id)
	return render(request, 'images/resource.html', {'resource': resource})

def tag(request, tag_name):
	tag = get_object_or_404(Tag, name=tag_name)
	tagged_items = TaggedItem.objects.filter(tag__id=tag.id)
	return render(request, 'images/tag.html', {'tag': tag, 'tagged_items': tagged_items})
	
