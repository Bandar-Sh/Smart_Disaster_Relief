from django.shortcuts import render
from rest_framework import viewsets
from .models import Drone, Location
from .serializers import DroneSerializer, LocationSerializer

# Create your views here.
class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
