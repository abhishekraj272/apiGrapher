from rest_framework import serializers
from . import models

class TopologySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topologies
        fields = ('id', 'topology', 'component', 'latency', 'capacity')

class UniqueTopologySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topologies
        fields = ('latency', 'capacity')