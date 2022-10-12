from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
#from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
#GenericAPIView
#from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

#ModelMixins Indivually
'''
class StudentList(GenericAPIView,ListModelMixin):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
    def get(self,request):
        return self.list(request)
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
    def post(self,request):
        return self.create(request)
class StudentDisplay(GenericAPIView,RetrieveModelMixin):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)

class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
'''
#Mixins Mixed
'''

class StudentLC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class StudentDUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
    '''
#Only With Api views
'''
class StudentList(ListCreateAPIView):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
# class StudentAdd(CreateAPIView):
#     queryset=Basic_model.objects.all()
#     serializer_class=Basic_serializer
class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer
'''
class StudentList(viewsets.ModelViewSet):
    queryset=Basic_model.objects.all()
    serializer_class=Basic_serializer