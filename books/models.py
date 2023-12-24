from django.contrib.auth.models import User
from django.db import models
from .forms import CreateUserForm

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='books/covers')
    file = models.FileField(upload_to='books/files')








   