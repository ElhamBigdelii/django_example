from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import datetime
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    '''Blog data model'''
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    created = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now_add=True)
    owner = models.OneToOneField('auth.User', verbose_name=_("Owner"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ("-created",)


class Post(models.Model):
    '''Post data model'''
    title = models.CharField(verbose_name=_("Title"), max_length=256)
    content = models.TextField(verbose_name=_("Content"))
    created = models.DateTimeField(verbose_name=_("Created"), auto_now=True)
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now=True)
    image = models.ImageField(verbose_name=_("Image"), upload_to="Post")
    blog = models.ForeignKey('Blog', verbose_name=_("Blog"), on_delete=models.CASCADE, related_name="posts")


    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ("-created",)
