from django import forms
from music.models import Music

GENRE_CHOICES = [
    ("KPOP", "K-POP"),
    ("HIPHOP", "힙합"),
    ("ROCK", "록"),
    ("POP", "팝"),
]



class MusicUploadForm(forms.ModelForm):

    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    class Meta:
        model = Music
        fields = ['title', 'genre', 'description', 'audio_file', 'cover_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cover_image'].required = False  # 선택사항으로
        self.fields['description'].required = False