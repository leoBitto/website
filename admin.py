from django.contrib import admin
from .models import Gallery_image,Contact,Opening_hour


class Gallery_imageAdmin(admin.ModelAdmin):
    list_display=('id', 'gallery_name', 'description', 'is_first', 'show_image')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'mail')


class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ('id', 'weekdays', 'weekend', 'closing_day')


admin.site.register(Gallery_image, Gallery_imageAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Opening_hour, OpeningHoursAdmin)