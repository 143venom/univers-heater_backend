from rest_framework import viewsets
from .models import *
from .serializers import *


class SiteLogoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteLogo.objects.all().order_by("-id")
    serializer_class = SiteLogoSerializer


class CompanyInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class FooterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Footer.objects.all().order_by("-id")
    serializer_class = FooterSerializer
