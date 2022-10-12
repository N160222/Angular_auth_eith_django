from django.forms import ModelForm
from django import forms
from .models import *
import re
class PostForm(ModelForm):
	class Meta:
		model = Post	
		#password = forms.CharField(widget=forms.PasswordInput)
		fields ='__all__'
		
	# this function will be used for the validation
	def clean(self):

		# data from the form is fetched using super function
		super(PostForm, self).clean()
		
		# extract the username and text field from the data
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		firstname = self.cleaned_data.get('firstname')
		phone = self.cleaned_data.get('phone')

		# conditions to be met for the username length
		if len(username) < 5:
			self._errors['username'] = self.error_class([
				'Minimum 5 characters required and unique'])
		if not(firstname.isalpha()):
			self._errors['firstname'] = self.error_class([
				'Only aplhabets'])
		if len(str(phone)) !=10:
			self._errors['phone'] = self.error_class([
				'Check Number'])
		if firstname.isnumeric():
			self._errors['phone'] = self.error_class([
				'Only Numbers'])
		# if len(text) <10:
		# 	self._errors['text'] = self.error_class([
		# 		'Post Should Contain a minimum of 10 characters'])
		# if len(password)<8:
		# 	self._errors['password'] = self.error_class([
		# 	'Password Should Contain a minimum of 8 characters'])
		reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
      
    # compiling regex
		pat = re.compile(reg)
		
		# searching regex                 
		mat = re.search(pat, password)
		if not mat:
			print("Not Mat")
			self._errors['password'] = self.error_class([
			'Password Should Contains minimum of 8 characters, small & capital alphabets and Special characters @$!#%*?&'])
		# return any errors if found
		return self.cleaned_data
class LoginForm(ModelForm):
	class Meta:
		model = Post	
		#password = forms.CharField(widget=forms.PasswordInput)
		fields =['username','password']