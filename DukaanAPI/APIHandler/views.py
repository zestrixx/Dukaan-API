from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


def Home(request):
    return render(request, 'home.html')


class OrderAPIView(APIView):

    def get(self, request):
        if not request.user.is_authenticated:
            next_url = request.path
            login_url = reverse('user-login') + '?next=' + next_url
            messages.warning(request, 'Please login to your account to access orders details.')
            return redirect(login_url)
        return render(request, 'dashboard.html')


@api_view(['GET'])
def UserDashboard(request):
    if not request.user.is_authenticated:
        next_url = request.path
        login_url = reverse('user-login') + '?next='+next_url
        messages.warning(request, 'Please login to your account to access dashboard')
        return redirect(login_url)
    return render(request, 'dashboard.html')
