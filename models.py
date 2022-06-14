from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Info(models.Model):
    email = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    photo = models.ImageField(
        upload_to='',
        null=True,
        blank=True,
    )
    date_updated = models.DateTimeField(
        auto_now=True,
    )