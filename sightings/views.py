from django.shortcuts import render
from django.http import HttpResponse

from .models import Sighting

def index(request):
    return HttpResponse('Project Squirrel')


