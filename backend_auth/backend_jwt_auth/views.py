from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('id','username')
class UserAPIView(RetrieveAPIView):
    permission_class=(IsAuthenticated)
    serializer_class=UserSerializer
    def get(self,request):
        return (self.request.user)


class LoginView():
    pass


