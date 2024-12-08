from celery import shared_task
import joblib
from .models import AudioData  # Adjust if needed
from .utils import transcribe_audio_from_db
from Alert_System.models import Alert
import re

# Load the saved model and vectorizer
model = joblib.load("ML_Models/text_classifier.pkl")
vectorizer = joblib.load("ML_Models/vectorizer.pkl")

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

@shared_task
def classify_text_task(audio_data_id):
    try:
        # Fetch the audio file from the database
        audio_data = AudioData.objects.get(id=audio_data_id)

        # Transcribe the audio file
        transcription = transcribe_audio_from_db(audio_data.audio_file.path)
        audio_data.transcription = transcription
        audio_data.save()

        # Classify the transcription
        if transcription and transcription not in ["Audio could not be understood.", "Error with the SpeechRecognition API"]:
            processed_text = preprocess_text(transcription)
            text_vectorized = vectorizer.transform([processed_text])
            
            # Get label and confidence score
            probabilities = model.predict_proba(text_vectorized)[0]
            label = model.predict(text_vectorized)[0]
            confidence_score = probabilities[label] * 100  # Convert to percentage
            
            # Update the classification result and confidence score
            audio_data.classification_result = "Emergency" if label == 1 else "Non-Emergency"
            audio_data.confidence_score = confidence_score
            audio_data.processed = True
            audio_data.save()

            # Generate an alert if the classification is "Emergency"
            if label == 1:
                Alert.objects.create(
                    audio_data=audio_data,
                    alert_type="Emergency Signal",
                    severity="High",
                    message=f"Detected Emergency signal: {transcription} with confidence {confidence_score:.2f}%"
                )
        else:
            audio_data.classification_result = "Unable to classify"
            audio_data.confidence_score = None
            audio_data.processed = True
            audio_data.save()

    except AudioData.DoesNotExist:
        print(f"AudioData with ID {audio_data_id} not found.")
