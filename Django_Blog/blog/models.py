from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    content = models.TextField()

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'
    
    def __repr__(self) -> str:
        return f'<{self.title}: {self.author} - {self.date_posted}'