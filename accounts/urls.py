from django.urls import path, include

from accounts.views import SignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
]