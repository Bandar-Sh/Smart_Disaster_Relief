import time
import whisper

def transcribe_audio_from_db(audio_file_path, retries=3, delay=5):
    # Load the Whisper model
    model = whisper.load_model("base") 

    for attempt in range(retries):
        try:
            # Perform transcription using Whisper
            result = model.transcribe(audio_file_path)
            transcription = result["text"]  # Extract transcription text
            return transcription

        except Exception as ex:
            if attempt < retries - 1:
                print(f"Retry {attempt + 1}/{retries} due to error: {ex}")
                time.sleep(delay)  # Wait before retrying
                continue
            else:
                return f"An error occurred during transcription after {retries} attempts: {ex}"

    return "Failed to transcribe audio after retries."
