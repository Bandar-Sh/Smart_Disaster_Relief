from django.apps import AppConfig


class AudioProcessingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Audio_Processing'

    def ready(self):
        import Audio_Processing.signals
