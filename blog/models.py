from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import datetime


class Blog(models.Model):
    '''Blog data model'''
    name = models.CharField(max_length = 100)
    created = models.DateTimeField(default = datetime.now)
    updated = models.DateTimeField(default = datetime.now)
    owner = models.OneToOneField('auth.User', on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    '''Post data model'''
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created = models.DateTimeField(auto_now = true)
    updated = models.DateTimeField(auto_now_add = true)
    image = odels.ImageField(upload_to = "Post")
    blog = models.ForeignKey('Blog', on_delete = models.CASCADE)

    def __str__(self):
        return self.title
