from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
import os

# Create your models here.


class Summer(models.Model):
    title = models.CharField(max_length=128)
    owner = models.CharField(max_length=32)
    content = RichTextField()

    def __str__(self):
        return self.title


class SummerImage(models.Model):
    img_description = models.CharField(max_length=128)
    artical_belong = models.ForeignKey(Summer)
    img = models.ImageField()

    def __str__(self):
        return self.img_description
