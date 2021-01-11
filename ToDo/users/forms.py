from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['description', 'due_date', 'priority']
        widgets = {
            'priority': forms.RadioSelect()
        }

class UpdateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['description', 'due_date', 'priority']
        widgets = {
            'priority': forms.RadioSelect()
        }
        