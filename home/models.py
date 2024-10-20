from django.db import models
from django.core.exceptions import ValidationError
from core.models import baseModel


# Create your models here.
class Slider(models.Model):
    ACTIVE = "A"
    INACTIVE = "I"
    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    ]
    
    image = models.ImageField(
        upload_to="home/sliders/",
        default="https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg",
        verbose_name="Slider Image",
        help_text="Upload an image for the slider. Default image will be used if none is provided.",
    )
    
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=ACTIVE,
        help_text="Status of the Slider",
    )

    class Meta:
        verbose_name_plural = "Sliders"  # Use plural form for consistency

    def clean(self):
        # Check if the image field is empty only if the default is not used.
        if not self.image or self.image == "https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg":
            raise ValidationError("An image is required for the slider.")

    def __str__(self):
        return f"Slider - {self.get_status_display()}"


class Choose(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="home/choose/",
        default="https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg",
        blank=True,
        null=True,
    )


class ChooseList(models.Model):
    icon = models.ImageField(
        upload_to="home/choose/",
        default="https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
