from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	# template = loader.get_template('tracking/index.html')
	return render(request, 'tracking/index.html')

def map_in(request):
    return render(request, 'tracking/map-in.html')

def map_out(request):
    return render(request, 'tracking/map-out.html')

def form_in(request):
    return render(request, 'tracking/form-in.html')

def form_out(request):
    return render(request, 'tracking/form-out.html')