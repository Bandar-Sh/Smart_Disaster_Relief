# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import AudioData
# from .serializers import AudioDataSerializer
# from .tasks import classify_text_task

# class AudioDataViewSet(viewsets.ModelViewSet):
#     queryset = AudioData.objects.all()
#     serializer_class = AudioDataSerializer


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import AudioData
from .serializers import AudioDataSerializer
from .tasks import classify_text_task

class AudioDataViewSet(viewsets.ModelViewSet):
  
    queryset = AudioData.objects.all()
    serializer_class = AudioDataSerializer

    def create(self, request, *args, **kwargs):
        """
        Override the create method to trigger transcription and classification tasks.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        audio_data = serializer.save()

        # Trigger the transcription and classification task
        classify_text_task.delay(audio_data.id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def trigger_classification(self, request, pk=None):
        try:
            audio_data = self.get_object()
            classify_text_task.delay(audio_data.id)
            return Response({"message": "Classification task triggered successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
