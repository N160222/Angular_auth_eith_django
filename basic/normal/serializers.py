from rest_framework import serializers
from .models import *

class Basic_serializer(serializers.ModelSerializer):

    class Meta:
        model=Basic_model
        fields="__all__"