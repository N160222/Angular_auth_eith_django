"""backend_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token,verify_jwt_token

# from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
# from backend_jwt_auth.views import UserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/auth/access-token/login/', obtain_jwt_token),
    path('accounts/auth/refresh-token/', refresh_jwt_token),
    path('accounts/auth/verify-token/', verify_jwt_token),
    path('',include('backend_jwt_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    
]
# path('api/token',TokenObtainPairView.as_view(),name='token_obtain_pair'),
#     path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
#     path('api/user',UserAPIView.as_view(),name='user')