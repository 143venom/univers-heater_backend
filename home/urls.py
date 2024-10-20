from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'slider', SliderViewSet, basename='slider')
router.register(r'choose', ChooseViewSet, basename='choose')
router.register(r'choose-list', ChooseListViewSet, basename='choose-list')

urlpatterns = [
    path('', include(router.urls)),
]