from django.urls import path, include
from .views import MusicUploadView, MusicListView, MusicDetailView, MusicLikeView, ChartView,GenreChartView

urlpatterns = [
    path('', MusicListView.as_view(), name="music-list"),
    path('detail/<int:id>/', MusicDetailView.as_view(), name="music-detail"),
    path('detail/<int:id>/like/', MusicLikeView.as_view(), name="music-like"),
    path('upload/', MusicUploadView.as_view(), name='music-upload'),
    path('chart/',ChartView.as_view(), name='chart'),
    path('chart/<str:genre>/', GenreChartView.as_view(), name='genre_chart'),

]