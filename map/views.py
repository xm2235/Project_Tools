from django.shortcuts import render
from sightings.models import Squirrel

def index(request):
    all_sightings = Squirrel.objects.all()[:100]
    context = {'all_sightings': all_sightings}
    return render(request, 'map/map.html', context)

# Create your views here.
