"""
URL configuration for DukaanAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from registration.views import UserRegistrationView, UserLoginView
from APIHandler.views import OrderAPIView, Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('api/user/register/', UserRegistrationView, name='user-registration'),
    path('api/user/login/', UserLoginView.as_view(), name='user-login'),
    path('api/user/logout/', LogoutView.as_view(next_page='user-login'), name='user-logout'),
    path('api/order/', OrderAPIView.as_view(), name='order-api'),
]
