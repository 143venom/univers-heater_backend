from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutList.objects.all()
    serializer_class = AboutListSerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class StoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class JourneyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer


class GoalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class VisionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vision.objects.all()
    serializer_class = VisionSerializer
