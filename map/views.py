from django.shortcuts import render
from sightings.models import Sighting

def index(request):
    all_sightings = Sighting.objects.all()[:100]
    context = {'all_sightings': all_sightings}
    return render(request, 'map/map.html', context)

# Create your views here.
