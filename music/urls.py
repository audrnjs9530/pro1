from django.urls import path, include
from .views import MusicUploadView, MusicListView, MusicDetailView, MusicLikeView, ChartView

urlpatterns = [
    path('', MusicListView.as_view(), name="music-list"),
    path('detail/<int:id>/', MusicDetailView.as_view(), name="music-detail"),
    path('detail/<int:id>/like/', MusicLikeView.as_view(), name="music-like"),
    path('upload/', MusicUploadView.as_view(), name='music-upload'),
    path('chart/',ChartView.as_view(), name='chart'),

]