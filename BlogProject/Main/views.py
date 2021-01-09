from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import NewPostForm, UserRegisterForm, PostUpdateForm
from .models import Post

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all()
    }
    return render(request, 'Main/home.html', context=context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'Main/about.html', context=context)

def author(request, author):
    user = User.objects.filter(username=author).first()
    posts = Post.objects.filter(author=user)
    context = {
        'title': 'Author\'s posts',
        'user': user,
        'posts': posts,
    }
    return render(request, 'Main/author.html', context)

def post_page(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    context = {
        'title': 'Post',
        'post': post
    }
    messages.success(request, post.id)
    return render(request, 'Main/post.html', context)

def new_post(request):
    author = request.user

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            post = Post()

            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.author = author

            post.save()
            return redirect('home')
    else:
        form = NewPostForm()

    context = {
        'title': 'New Post',
        'form': form,
    }
    return render(request, 'Main/new_post.html', context)

def update(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    author = post.author

    if request.method == 'POST':
        form = PostUpdateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.author = author
            post.save()
            
            return redirect('home')

    else:
        form = PostUpdateForm()

    context = {
        'title': 'Update Post',
        'post': post,
        'form': form,
    }
    return render(request, 'Main/update.html', context)
    
def delete(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    context = {
        'title': 'Delete Post',
        'post': post,
    }
    post.delete()
    return render(request, 'Main/delete.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, message=f'Account created for {username}')

            return redirect('profile')
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'Main/register.html', context=context)

@login_required
def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'Main/profile.html', context=context)
    