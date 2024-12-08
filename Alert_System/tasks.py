from .models import Alert

def generate_and_save_alert(drone, transcription):
   
    message = f"Distress detected from {drone.name}: {transcription}"
    alert = Alert.objects.create(drone=drone, message=message)
    alert.save()
    print(f"ALERT SAVED: {message}")
    return alert
