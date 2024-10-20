from django.db import models
from core.models import *
from ckeditor.fields import RichTextField


# Create your models here.
class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Title",
        help_text="The main title for the About section.",
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name="Subtitle",
        help_text="The subtitle for the About section.",
    )
    description = RichTextField(
        verbose_name="Description",
        help_text="A detailed description of the About section.",
    )
    image = models.ImageField(
        upload_to="about/about/",
        verbose_name="Image",
        help_text="Upload an image for the About section.",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About"
        ordering = ["title"]


class AboutList(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Title", help_text="The title for the About List."
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About List"
        ordering = ["title"]


class Team(baseModel):
    name = models.CharField(
        max_length=255, verbose_name="Name", help_text="The name of the team member."
    )
    profession = models.CharField(
        max_length=255,
        verbose_name="Profession",
        help_text="The profession or role of the team member.",
    )
    description = RichTextField(
        verbose_name="Description", help_text="A description of the team member."
    )
    image = models.ImageField(
        upload_to="about/team/",
        verbose_name="Image",
        help_text="Upload an image of the team member.",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Team Member"
        ordering = ["name"]


class Testimonial(baseModel):
    RATING_CHOICES = [
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    ]

    name = models.CharField(max_length=255, verbose_name="Name")
    position = models.CharField(
        max_length=255, verbose_name="Position", blank=True, null=True
    )
    testimonial = models.TextField(verbose_name="Testimonial")
    image = models.ImageField(
        upload_to="testimonials/", verbose_name="Image", blank=True, null=True
    )
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Rating")

    class Meta:
        verbose_name_plural = "Testimonials"
        ordering = ["-posted_at"]

    def __str__(self):
        return f"Testimonial by {self.name} - {self.rating} Stars"


class Story(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    image = models.ImageField(
        upload_to="about/stories/", verbose_name="Image", blank=True, null=True
    )


class Journey(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    image = models.ImageField(
        upload_to="about/journey/", verbose_name="Image", blank=True, null=True
    )


class Goal(models.Model):
    content = RichTextField(verbose_name="Content")


class Vision(models.Model):
    content = RichTextField(verbose_name="Content")
    
