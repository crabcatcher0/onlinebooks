from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

 
class RegisterUser(UserCreationForm):
     class Meta:
          model = User
          fields = ['first_name', 'last_name', 'username', 'email',  'password1', 'password2']
        

class LoginUser(AuthenticationForm):
     email = forms.EmailField()
     password = forms.CharField(max_length=30, widget=(forms.PasswordInput()))