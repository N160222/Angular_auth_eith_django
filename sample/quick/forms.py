from django import forms  
from .models import Employee 
from django.forms import fields  
from django.db import models 


# class StudentForm(forms.Form):  
#     firstname = forms.CharField(label="Enter first name",max_length=50)  
#     lastname  = forms.CharField(label="Enter last name", max_length = 100)  

# class InputForm(forms.Form):
 
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField()
#     password = forms.CharField(widget = forms.PasswordInput())
 
  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Employee  
        # It includes all the fields of model  
        fields = '__all__'   