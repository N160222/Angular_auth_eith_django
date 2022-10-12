'''from django.shortcuts import render
from . import forms

#DataFlair #Form #View Functions
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
    else:
        html = 'welcome for first time'
    return render(request, 'index.html', {'html': html, 'form': form})'''
from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse
# Create your views here.

#DataFlair #AJAX_tutorial
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', { 'posts': posts })

def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id = post_id )
        m = Like( post=likedpost )
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")