from rest_framework import serializers
from .models import *


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class AboutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutList
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = "__all__"

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ["content"]

class VisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vision
        fields = ["content"]
