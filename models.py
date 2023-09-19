from django.db import models
from django.utils.html import format_html

### information models
class Gallery_image(models.Model):
    gallery_name = models.CharField(max_length=100)
    header = models.CharField(max_length=100, default="", blank=True, null=True)
    description = models.CharField(max_length=300, default="", blank=True, null=True)
    img = models.ImageField(upload_to="", blank=True, null=True)
    is_first = models.BooleanField(default=False)


    def show_image(self):
        return format_html('<img src="{}" style="height:100px;" />', self.img.url)


class Contact(models.Model):
    phone = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return "Contacts"


class Opening_hour(models.Model):
    weekdays = models.CharField(max_length = 200, blank=True, null=True)
    weekend = models.CharField(max_length=300, blank=True, null=True)
    closing_day = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return "Opening hours"