# 프로젝트 메인 urls.py (예: config/urls.py)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # 1. 이 줄이 있는지 확인
from django.conf.urls.static import static # 2. 이 줄이 있는지 확인

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
    path('accounts/', include('accounts.urls')),
]

# 3. 중요: 아래 문장을 urlpatterns 끝에 추가해야 합니다.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)