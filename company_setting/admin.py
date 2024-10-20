from django.contrib import admin
from .models import *


class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ("logo", "favicon")


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "email",
        "phone",
        "address",
    )


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("facebook", "twitter", "linkedin", "instagram", "youtube")


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'copyright')


admin.site.register(SiteLogo, SiteLogoAdmin)
admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Footer, FooterAdmin)
