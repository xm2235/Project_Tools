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

