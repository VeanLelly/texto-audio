from rest_framework.views import APIView
from rest_framework.response import Response
from gtts import gTTS

class TextToAudioView(APIView):
    def post(self, request):
        from .serializers import TextToAudioSerializer

        serializer = TextToAudioSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            language = serializer.validated_data['language']

            # TODO: Converter texto em áudio
            tts = gTTS(text= text, lang=language)
            file_path = "audio_output.mp3"
            tts.save( file_path )

            return Response({'message': 'Áudio gerado!', 'file_url': f'/media/{file_path}'})
        return Response(serializer.errors)