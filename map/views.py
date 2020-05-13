from django.shortcuts import render
from sightings.models import Sighting

def index(request):
    all_sightings = Sighting.objects.all()[:50]  
    return render(request, 'map/map.html', {'all_sightings': all_sightings})


# Create your views here.
