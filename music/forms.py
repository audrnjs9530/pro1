from django import forms
from music.models import Music



class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'genre', 'description', 'audio_file', 'cover_image']
