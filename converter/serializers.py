from rest_framework import serializers

class TextToAudioSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
    language = serializers.ChoiceField(choices=[('en', 'English'), ('pt', 'Portuguese')], default='pt')