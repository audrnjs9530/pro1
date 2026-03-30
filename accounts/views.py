from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm


class SignUpView(View):
    def get(self, request):
        return render(
            request, 'registration/sign_up.html',
            {'form': CustomUserCreationForm})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('music-list')