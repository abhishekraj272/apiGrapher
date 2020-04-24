from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Topologies
from django.http import Http404
from rest_framework import status
from django.shortcuts import render

def index(request):
    return render(request, "api/index.html")

class TopologyFiltered(APIView):
    def get(self, request, query):
        print(query)
        query_set = Topologies.objects.filter(topology=query)
        serializer = serializers.UniqueTopologySerializer(query_set, many=True)
        return Response(serializer.data)

class Topology(APIView):
    def get(self, request):
        query_set = Topologies.objects.all()
        serializer = serializers.TopologySerializer(query_set, many=True)
        return Response(serializer.data)