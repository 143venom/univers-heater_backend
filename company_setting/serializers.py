from rest_framework import serializers
from .models import *


class SiteLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteLogo
        fields = "__all__"


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = "__all__"


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = "__all__"
