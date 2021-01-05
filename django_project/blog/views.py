from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Hassan Aziz',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Hassan Aziz',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Hassan Aziz',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2019'
    }
]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})