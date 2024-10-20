from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )
    image = models.ImageField(
    upload_to="blog/",
    validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
      ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


    MAX_IMAGE_SIZE_MB = 5

    def clean(self):
        if not self.image:
            raise ValidationError("An image is required for the service.")
        
        if self.image and self.image.size > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
            raise ValidationError(f"Image size should not exceed {self.MAX_IMAGE_SIZE_MB} MB.")
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.create_slug(self.title)
        super().save(*args, **kwargs)

    @staticmethod
    def create_slug(title):
        slug = slugify(title)
        original_slug = slug
        counter = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1
        return slug


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    author = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        if self.parent:
            return f"Reply to Comment {self.parent.id} by {self.author} on {self.blog.title}"
        else:
            return f"Comment {self.id} by {self.author} on {self.blog.title}"
