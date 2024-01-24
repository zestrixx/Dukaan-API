from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.urls import reverse

def UserRegistrationView(request):
    return Response({'status: registeration in progress'})


class UserLoginView(LoginView):
    def get_success_url(self):
        return reverse('home')