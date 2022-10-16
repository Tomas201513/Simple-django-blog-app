
from django import forms 
from django.contrib.auth.forms import UserCreationForm #default user form by django
from django.contrib.auth.models import User # place to store different users
from .models import Post

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
   
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","description"]