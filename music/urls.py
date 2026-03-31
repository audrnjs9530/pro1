from django.urls import path, include
from .views import MusicUploadView, MusicListView, MusicDetailView

urlpatterns = [
    path('', MusicListView.as_view(), name="music-list"),
    path('detail/<int:id>/', MusicDetailView.as_view(), name="music-detail"),
    path('upload/', MusicUploadView.as_view(), name='music-upload'),
]