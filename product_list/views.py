from django.shortcuts import render, render_to_response
from .models import Product_spec

# Create your views here.

def show(request):

	project = Product_spec.objects.all()
	return render_to_response('open.html', {'project': project})
