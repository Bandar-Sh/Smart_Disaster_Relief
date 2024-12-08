from django.db import models
from Drone_Management.models import Drone

# Create your models here.


class RealTimeData(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Real-time data from {self.drone.name}"