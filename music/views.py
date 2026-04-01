from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import permissions, generics
from rest_framework.exceptions import PermissionDenied

from .forms import MusicUploadForm, GENRE_CHOICES
from .models import Music
from django.db.models import Count, F, ExpressionWrapper, IntegerField
from .serializers import MusicSerializer
from django.contrib.auth.mixins import LoginRequiredMixin


class MusicUploadView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'


    def get(self, request):
        context = {
            'form': MusicUploadForm,
        }
        return render(request, "upload.html", context)

    def post(self, request):
        form = MusicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)   # DB 저장 보류
            music.artist = request.user  # artist는 유저에서 가져오므로 직접 지정
            music.save()
            return render(request, 'detail.html', {"music": music})
        else:
            return render(request, "upload.html", {"form": form})


class MusicDetailView(View):
    def get(self, request, id):
        music = Music.objects.get(id=id)
        is_liked = music.likes.filter(id=request.user.id).exists()
        session_key = f"viewed_music_{id}"
        if not request.session.get(session_key):
            music.play_count += 1
            music.save(update_fields=["play_count"])
            request.session[session_key] = True

            request.session.set_expiry(30)

        context = {'music': music, 'is_liked': is_liked}

        return render(request, "detail.html", context)

class MusicListView(View):
    def get(self, request):
        music_list = Music.objects.all().order_by('-created_at')
        return render(request, "list.html", {"music_list": music_list})


class MusicLikeView(LoginRequiredMixin ,View):
    login_url = '/accounts/login/'
    def post(self, request, id):
        music = get_object_or_404(Music, id=id)
        if request.user in music.likes.all():
            music.likes.remove(request.user)  # 취소
        else:
            music.likes.add(request.user)

        is_liked = music.likes.filter(id=request.user.id).exists()
        like_count = music.likes.count()
        context = {'music': music, 'is_liked': is_liked, 'like_count': like_count}
        return render(request, 'detail.html', context)


class ChartView(View):
    def get(self, request, *args, **kwargs):
        musics = Music.objects.annotate(
            like_count=Count('likes'),
            score=ExpressionWrapper(
                F('like_count') * 3 + F('play_count'),
                output_field=IntegerField()
            )
        ).order_by('-score')

        return render(request, 'chart.html', {'musics': musics, "genres" : GENRE_CHOICES})


class GenreChartView(View):
    def get(self, request, genre):
        musics = Music.objects.filter(genre=genre).annotate(
            like_count=Count('likes'),
            score=ExpressionWrapper(
                F('like_count') * 3 + F('play_count'),
                output_field=IntegerField()
            )
        ).order_by('-score')

        return render(request, "chart.html", {
            "genre": genre,
            "musics": musics,
            "genres": GENRE_CHOICES,
        })