from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
#    path('<unique_squirrel_id>/', views.update),
#    path('add/', views.add),
    path('stats/', views.stats),

]

