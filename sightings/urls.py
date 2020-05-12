from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<uique_squirrel_id>', views.update),
    path('add', views.add),
    path('stats/', views.get_stats),

]

