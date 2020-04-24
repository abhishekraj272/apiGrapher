from django.contrib import admin 
from django.urls import path
from .views import Topology, index, TopologyFiltered
  
urlpatterns = [ 
    path('topology/<str:query>', TopologyFiltered.as_view()),
    path('topology/', Topology.as_view()),
    path('', index),
] 