from django.shortcuts import render,redirect
from .forms import *
from .models import Employee 
#File upload
from .functions.functions import handle_uploaded_file 
# Create your views here.
def home_view(request):
    context ={}
    #context['form']= InputForm()
    # context['form']= InputForm()
    return render(request, "index.html", context)


# def index(request):  
#     student = StudentForm()  
#     return render(request,"index.html",{'form':student})  
# def emp(request):
#     if request.method == "POST":  
#         form = EmployeeForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 print("It is Valid!!!!!")
#                 return redirect('/')  
#             except:  
#                 print("It is not Valid!!!!!")
#     else:  
#         print("It is not POST!!!!!")
#         form = EmployeeForm()  
#     return render(request,'index.html',{'form':form})  



  
def emp(request):  
    if request.method == 'POST':  
        form = EmployeeForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
            handle_uploaded_file(request.FILES['file'])    
            return render(request, 'index.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = EmployeeForm()  
  
    return render(request, 'index.html', {'form': form}) 