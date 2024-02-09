from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response


def Home(request):
    return render(request, 'home.html')


class OrderAPIView(APIView):

    def get(self, request):
        if not request.user.is_authenticated:
            next_url = request.path
            login_url = reverse('user-login') + '?next=' + next_url
            return redirect(login_url)
        return render(request, 'dashboard.html')
        
