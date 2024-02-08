from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


def Home(request):
    return render(request, 'home.html')


class OrderAPIView(APIView):

    def get(self, request):
        if not request.user.is_authenticated:
            next_url = request.build_absolute_uri()
            login_url = reverse('user-login') + '?next=' + next_url
            return redirect(login_url)
        return Response({'message': 'Order received successfully'})
        
