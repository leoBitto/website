from django import forms
from .models import Gallery_image, Contact, Opening_hour

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = Gallery_image
        fields = ['gallery_name', 'description', 'img', 'is_first']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone', 'mail']

class OpeningHourForm(forms.ModelForm):
    class Meta:
        model = Opening_hour
        fields = ['weekdays', 'weekend', 'closing_day']
