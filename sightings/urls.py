from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<unique_squirrel_id>/', views.unique),
#    path('add/', views.add),
    path('stats/', views.stats),

]

