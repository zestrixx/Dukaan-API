from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from registration.views import UserRegistrationAPIView, UserLoginAPIView
from APIHandler.views import OrderAPIView, Home
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
    path('api/order/', OrderAPIView.as_view(), name='order-api'),
    path('dashboard/', OrderAPIView.as_view(), name='order-api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
