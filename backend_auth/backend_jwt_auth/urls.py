from django.urls import path,include
from .views import *

# from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
# from backend_jwt_auth.views import UserAPIView

urlpatterns = [
    # path('api/token',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/user',UserAPIView.as_view(),name='user')
]
