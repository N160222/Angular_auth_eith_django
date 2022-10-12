
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse
from . import views
 
 
urlpatterns = [
    path('', views.home, name ='index'),
    path('login/', views.home, name ='login'),
]