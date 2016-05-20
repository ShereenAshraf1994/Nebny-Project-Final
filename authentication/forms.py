from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

	class Meta:
 		model= User
 		fields = {'username','email','password1','password2','first_name','last_name'}

def save(self):
 	
 	user = User.objects.create_user(
				username=self.cleaned_data['username'],
				password1=self.cleaned_data['password1'],
				password2=self.cleaned_data['password2'],
				email=self.cleaned_data['email'],
				first_name=self.cleaned_data['first_name'],
				last_name=self.cleaned_data['last_name'])
 	return user

class PasswordForm(UserCreationForm):
	model = User
	fields = {'password1','password2','username'}

	def save(self):
 		user=User.objects.get(username=form.username)
 		user = user.set_password(
 				
				password1=self.cleaned_data['password1'],
				password2=self.cleaned_data['password2'])
				
 		return user
