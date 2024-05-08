from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import UserRegistrationSerializer, UserLoginSerializer

class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user and request.user.is_authenticated:
            messages.info(request, 'You are already logged in!')
            return redirect('home')
        serializer = UserRegistrationSerializer()
        context = {'serializer': serializer}
        return render(request, 'register.html', context)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user) # type: ignore
            return redirect('user-login')
        return Response(serializer.errors, status=400)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        if request.user and request.user.is_authenticated:
            messages.info(request, 'You are already logged in!')
            return redirect('home')
        serializer = UserLoginSerializer()
        context = {'serializer':serializer}
        return render(request, 'registration/login.html', context)

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username'] # type: ignore
            password = serializer.validated_data['password'] # type: ignore

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                next_url = request.POST.get('next')
                print(next_url)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('home')
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)