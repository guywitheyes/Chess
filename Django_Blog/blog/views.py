from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', context={'title': 'Homepage', 'posts': posts})

def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})

def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        
        messages.success(request, f'Account created for {username}!')
        return redirect('blog-home')

    return render(request, 'blog/register.html', context={'title': 'Register', 'form': form})