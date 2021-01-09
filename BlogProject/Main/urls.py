from os import name
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='Main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Main/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),

    path('author/<str:author>', views.author, name='author'),
    path('posts/<int:post_id>', views.post_page, name='post'),
    path('posts/new', views.new_post, name='new-post'),

    path('posts/<int:post_id>/update', views.update, name='update'),
    path('posts/<int:post_id>/delete', views.delete, name='delete'),
]
