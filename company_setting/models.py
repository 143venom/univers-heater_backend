from django.db import models


# Logo Settings
class SiteLogo(models.Model):
    logo = models.ImageField(
        upload_to="company/logo/",
        default="default/favicon.ico",
        blank=True,
        null=True,
        verbose_name="Company Logo",
        help_text="Upload the logo of the company",
    )
    favicon = models.ImageField(
        upload_to="company/logo/",
        default="default/favicon.ico",
        blank=True,
        null=True,
        verbose_name="Favicon",
        help_text="Upload the favicon for the website",
    )

    def __str__(self):
        return "Site Logo Settings"

    class Meta:
        verbose_name_plural = "Site Logo"


# Contact Settings
class CompanyInfo(models.Model):
    company_name = models.CharField(
        max_length=255,
        verbose_name="Company Name",
        help_text="The full name of the company",
    )
    email = models.EmailField(
        verbose_name="Email Address", help_text="The main contact email for the company"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Phone Number",
        help_text="The main contact phone number for the company",
    )
    address = models.CharField(
        max_length=700,
        verbose_name="Street Address",
        help_text="The street address of the company",
        default="Your Address",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.company_name} - {self.phone}"

    class Meta:
        verbose_name_plural = "Company Information"



# Footer Setting
class Footer(models.Model):
    copyright = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Copyright Text",
        help_text="The copyright notice to display in the footer",
    )

    def __str__(self):
        return "Footer Settings"

    class Meta:
        verbose_name_plural = "Footer"
