# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'site-logo', SiteLogoViewSet, basename='blogs')
router.register(r'company-info', CompanyInfoViewSet, basename='company-info')
router.register(r'footer', FooterViewSet, basename='footer')

urlpatterns = [
    path('', include(router.urls)),
]