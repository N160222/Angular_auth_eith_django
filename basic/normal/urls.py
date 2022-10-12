from django.urls import path,include
from .models import *
from .serializers import *
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('api',StudentList,basename="student")

urlpatterns = [
        path('', include(router.urls)),
        #path('api/',StudentList.as_view()),
        
]
'''
    path('add/',StudentCreate.as_view()),
    path('dis/<int:pk>',StudentDisplay.as_view()),
    path('up/<int:pk>',StudentUpdate.as_view()),
    '''

'''
path('slc/',StudentLC.as_view()),
    
    path('dud/<int:pk>',StudentDUD.as_view()),
    '''