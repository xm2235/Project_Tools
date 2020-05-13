from django.shortcuts import render
from sightings.models import Sighting

def index(request):
    sightings = Sighting.objects.all()[:100]
    return render(request, 'map/map.html', {'sightings': sightings})


# Create your views here.
