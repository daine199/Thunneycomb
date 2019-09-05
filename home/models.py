from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Entrance(models.Model):
    entrance = models.CharField(max_length=32)
    entrance_url = models.CharField(max_length=1024)

    def __str__(self):
        return self.entrance


class Switch(models.Model):
    switch_key = models.CharField(max_length=128)
    switch_value = models.BooleanField(default=False, verbose_name="Status")

    def __str__(self):
        return str(self.switch_value)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=17, blank=True)
    department = models.CharField(max_length=200, default='Thunneycomb Address', blank=True)

    def __str__(self):
        return self.user.username

