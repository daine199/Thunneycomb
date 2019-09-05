from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.


class Platycodon(models.Model):
    author = models.CharField(max_length=20, verbose_name="作者")
    title = models.CharField(max_length=128)
    content = RichTextUploadingField()
    update_time = models.DateTimeField(auto_now=True, verbose_name='Update Time')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def __str__(self):
        return self.title


class PlatycodonTag(models.Model):
    platycodon_id = models.IntegerField(default=0, verbose_name="Platycodon ID")
    tag_name = models.CharField(max_length=20, default="公共标签", verbose_name="Platycodon Tag Name")

    def __str__(self):
        return self.tag_name

