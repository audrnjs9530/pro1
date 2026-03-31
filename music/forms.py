from django import forms
from music.models import Music



class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'genre', 'description', 'audio_file', 'cover_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cover_image'].required = False  # 선택사항으로
        self.fields['description'].required = False