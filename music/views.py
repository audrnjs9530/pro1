from django.shortcuts import render
from django.views import View
from rest_framework import permissions, generics
from rest_framework.exceptions import PermissionDenied

from .forms import MusicUploadForm
from .models import Music
from .serializers import MusicSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# class MusicUploadView(generics.CreateAPIView):
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#                 #              serializer_class의 값
#     def perform_create(self, serializer):
#         user = self.request.user
#         if not user.is_artist:
#             raise PermissionDenied('아티스트 계정만 업로드 가능합니다.')
#         serializer.save(artist=user)

# 업로드를 하면 그대로 music 모델에 저장되어 늘어남
# serializer에 save를 하는데 왜? -> serializers.py에서 model=Music 을 하기 때문에 save하면 music 모델이 추가가 된다.


class MusicUploadView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'


    def get(self, request):
        context = {
            'form': MusicUploadForm,
        }
        return render(request, "upload.html", context)

    def post(self, request):
        return


class MusicDetailView(View):
    def get(self, request, id):
        music = Music.objects.get(id=id)
        return render(request, "detail.html", {"music": music})

class MusicListView(View):
    def get(self, request):
        music_list = Music.objects.all().order_by('-created_at')
        return render(request, "list.html", {"music_list": music_list})
