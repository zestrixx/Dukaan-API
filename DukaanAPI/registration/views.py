from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.urls import reverse


def UserRegistrationView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            token, created = Token.objects.get_or_create(user=user)
            # Redirect to user's dashboard or any other page
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


class UserLoginView(LoginView):
    def get_success_url(self):
        return reverse('home')

    def form_invalid(self, form):
        return Response({'message': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
