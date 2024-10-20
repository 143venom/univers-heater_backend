from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ("image_preview",)  # Add a trailing comma to define a tuple

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="50" />', obj.image.url
            )
        return "No image"

    image_preview.short_description = "Image Preview"

# Register the model with the admin interface
admin.site.register(Slider, SliderAdmin)
admin.site.register(Choose)
admin.site.register(ChooseList)
