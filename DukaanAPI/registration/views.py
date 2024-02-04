from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer

class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = UserRegistrationSerializer()
        context = {'serializer': serializer}
        return render(request, 'register.html', context)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return redirect('user-login')
        return Response(serializer.errors, status=400)