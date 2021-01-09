from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']

class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']