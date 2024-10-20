# myapp/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactForm

@receiver(post_save, sender=ContactForm)
def send_contact_form_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Contact Form Submission'
        message = f"""
        New contact form submission:

        Name: {instance.first_name} {instance.last_name}
        Email: {instance.email}
        Phone Number: {instance.phone_number}
        
        Message:
        {instance.message}
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['recipient_email@example.com'],  # Add your recipient's email here
            fail_silently=False,
        )
