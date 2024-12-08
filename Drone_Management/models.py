from django.db import models

# Create your models here.

class Drone(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.drone.name} at {self.timestamp}"
