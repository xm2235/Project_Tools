from django.urls import path

from . import views

#app_name = 'sightings'

urlpatterns =[
    path('',views.index,name = 'index'),

    path('stats/',views.stats,name = 'stats'),
]
