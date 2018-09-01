from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View, TemplateView, 
								  ListView, DetailView,
								  CreateView, UpdateView,
								  DeleteView)
from basic_app import models


class IndexView(TemplateView):
	context_object_name='index'
	template_name='index.html'

# Create your views here.
# most basic way
class SchoolListView(ListView):
	context_object_name = 'schools'
	model= models.School


class SchoolDetailView(DetailView):
	context_object_name = 'school_detail'
	model = models.School
	template_name = 'basic_app/school_detail.html'	


class SchoolCreateView(CreateView):
	fields = ('name','principle','location')
	model = models.School # refers to models.py School class model

class SchoolUpdateView(UpdateView):
	fields = ('name','principle')
	model = models.School

class SchoolDeleteView(DeleteView):
	model = models.School
	success_url = reverse_lazy("basic_app:list") # once u deleted a school,
												 # go back to the list view (the class SchoolListView above)

class StudentCreateView(CreateView):
	fields = ('name','age','school')
	model = models.Student # refers to models.py School class model