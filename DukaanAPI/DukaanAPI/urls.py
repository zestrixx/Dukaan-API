from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from registration.views import UserRegistrationAPIView, UserLoginAPIView
from APIHandler.views import OrderAPIView, Home, UserDashboard
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('auth/register/',  UserRegistrationAPIView.as_view(), name='user-registration'),
    path('auth/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('auth/logout/', LogoutView.as_view(next_page='user-login'), name='user-logout'),
    path('user/dashboard/', UserDashboard, name='user-dashboard'),
    path('api/order/', OrderAPIView.as_view(), name='order-api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
