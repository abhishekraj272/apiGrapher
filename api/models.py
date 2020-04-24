from django.db import models

# Create your models here.
class Topologies(models.Model):
    topology = models.CharField(max_length=50)
    component = models.CharField(max_length=50)
    latency = models.FloatField()
    capacity = models.FloatField()

    def __str__(self):
        return  self.topology