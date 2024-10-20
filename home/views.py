from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *


class SliderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class ChooseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Choose.objects.all()
    serializer_class = ChooseSerializer


class ChooseListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChooseList.objects.all()
    serializer_class = ChooseListSerializer
