from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = [
            'id', 'title', 'description', 'genre',
            'audio_file', 'cover_image', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']