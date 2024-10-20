from django.forms import ValidationError
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactForm, CompanyInfo
from .serializers import ContactFormSerializer, CompanyInfoSerializer
import logging

logger = logging.getLogger(__name__)

def send_contact_form_email(contact_form):
    subject = 'New Contact Form Submission'
    message = (
        f"Name: {contact_form.first_name} {contact_form.last_name}\n"
        f"Email: {contact_form.email}\n"
        f"Phone Number: {contact_form.phone_number}\n"
        f"Message:\n{contact_form.message}"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [settings.COMPANY_EMAIL]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        raise APIException(_("Could not send email notification."))

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        try:
            contact_form = serializer.save()
            send_contact_form_email(contact_form)
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            raise APIException(_("Validation error occurred. Please check your input."))
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise APIException(_("An unexpected error occurred."))

class CompanyInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
