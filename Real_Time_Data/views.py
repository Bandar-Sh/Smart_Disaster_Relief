from django.shortcuts import render
from rest_framework import viewsets
from .models import RealTimeData
from .serializers import RealTimeDataSerializer

class RealTimeDataViewSet(viewsets.ModelViewSet):
    queryset = RealTimeData.objects.all()
    serializer_class = RealTimeDataSerializer
