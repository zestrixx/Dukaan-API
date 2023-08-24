from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


def Home(request):
    return render(request, 'home.html')


class OrderAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Process the incoming order data here
        return Response({'message': 'Order received successfully'})
