from django.db import models

# Create your models here.


class PetAPI(models.Model):
    user = models.CharField(max_length=32)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.user
