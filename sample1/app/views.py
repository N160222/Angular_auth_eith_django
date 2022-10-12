from .models import Post
from .forms import PostForm
from .import views
from django.shortcuts import HttpResponse, render, redirect


def home(request):
    if request.method =='GET':
        details = PostForm()
        return render(request, "home.html",{'form':details})

	# check if the request is post
    if request.method =='POST':

        details = PostForm(request.POST)

        if details.is_valid():

            post = details.save(commit = False)
            post.save()

            return render(request, "home.html", {'form':details})
            
        else:
        
            return render(request, "home.html", {'form':details})
    else:

        
        form = PostForm(None)
        return render(request, 'home.html', {'form':form})

def login_set(request):
    if request.method =='GET':
        details = LoginForm()
        return render(request, "home.html",{'form':details})

