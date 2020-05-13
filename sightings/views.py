from django.shortcuts import render
from django.http import HttpResponse

from .models import Sighting

def index(request):
    all_sightings = Sighting.objects.all()
    return render(request, 'sightings/index.html', {'all_sightings': all_sightings})

def unique(request, unique_squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_id = unique_squirrel_id)
    return render(request, 'sightings/unique.html', {'squirrel' : squirrel})

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
