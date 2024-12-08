from django.db import models
from Audio_Processing.models import AudioData
# Create your models here.


class Alert(models.Model):
    audio_data = models.ForeignKey(AudioData, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=50)
    severity = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert {self.id} - {self.alert_type} ({self.severity})"
