from django.shortcuts import render, render_to_response
from .models import Project_spec

# Create your views here.

def show(request):

	project = Project_spec.objects.all()
	return HttpResponse(resp)
