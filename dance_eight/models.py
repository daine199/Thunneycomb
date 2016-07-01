from django.db import models
from django.contrib import admin

# Create your models here.


class DanceEightManager(models.Model):
    dance_eight_site_name = models.CharField(max_length=20)
    dance_eight_owner = models.CharField(max_length=20)
    dance_eight_owner_email = models.EmailField(blank=True)
    dance_eight_fav_ico = models.ImageField(name="fav_ico")
    dance_eight_logo = models.ImageField(name="logo", )

    def __str__(self):
        return self.dance_eight_site_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name


class Classification(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return "{0}".format(self.name)


class Article(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=50, blank=True, )
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author)
    classification = models.ForeignKey(Classification)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()

    def __str__(self):
        return "{0}".format(self.caption)