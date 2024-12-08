from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AudioData
from .tasks import classify_text_task

@receiver(post_save, sender=AudioData)
def process_audio_on_save(sender, instance, created, **kwargs):
    if created:
        classify_text_task.delay(instance.id)
