from django.db import models
from Drone_Management.models import Drone
# Create your models here.


class AudioData(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/')
    transcription = models.TextField(null=True, blank=True)
    classification_result = models.CharField(max_length=50, null=True, blank=True)
    confidence_score = models.FloatField(null=True, blank=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audio {self.id} from {self.drone.name}"
