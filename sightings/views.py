from django.shortcuts import render
from django.http import HttpResponse

from .models import Sighting

def index(request):
    return HttpResponse('Project Squirrel')

def update(request, unique_squirrel_id):
    return HttpResponse('update section')

def add(request):
    return HttpResponse('add section')

def get_stats(request):
    return HttpResponse('stats section')

def stats(request): 
	stats1=Sighting.objects.all().count() 
	stats2=Sighting.objects.filter(age='Adult').count() 
	stats3=Sighting.objects.filter(age='Juvenile').count() 
	stats4=Sighting.objects.filter(running=True).count() 
	stats5=Sighting.objects.filter(eating=True).count() 
	
	value = { 
	'Stats1':stats1, 
	'Stats2':stats2, 
	'Stats3':stats3, 
	'Stats4':stats4, 
	'Stats5':stats5, 
	} 
	return render(request, 'sightings/stats.html', value)  
