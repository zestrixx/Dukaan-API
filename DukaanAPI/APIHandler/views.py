from django.shortcuts import render
# from rest_framework import generics
from rest_framework.views import APIView
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def Home(request):
    return render(request, 'home.html')


class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Order received successfully'})
