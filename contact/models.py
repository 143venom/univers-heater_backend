from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class ContactForm(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    email = models.EmailField(verbose_name=_("Email Address"))
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', _("Enter a valid phone number."))],
        verbose_name=_("Phone Number")
    )
    message = models.TextField(verbose_name=_("Message"))

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        ordering = ['-id']
        verbose_name = _("Contact Form")
        verbose_name_plural = _("Contact Forms")


class CompanyInfo(models.Model):
    address = models.TextField(verbose_name=_("Address"))
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', _("Enter a valid phone number."))],
        verbose_name=_("Phone Number")
    )
    email = models.EmailField(verbose_name=_("Email Address"))

    def __str__(self):
        return f"Company Info - Email: {self.email}"

    class Meta:
        verbose_name = _("Company Info")
        verbose_name_plural = _("Company Infos")
