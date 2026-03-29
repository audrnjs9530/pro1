from django.urls import path, include
from .views import MusicUploadView

urlpatterns = [
    path('upload/', MusicUploadView.as_view(), name='music-upload'),
]