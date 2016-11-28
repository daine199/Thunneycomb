from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.


class Platycodon(models.Model):
    title = models.CharField(max_length=128)
    content = RichTextUploadingField()
    update_time = models.DateTimeField(auto_now=True, verbose_name='Update Time')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def __str__(self):
        return self.title

