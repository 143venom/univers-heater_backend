from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class ChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choose
        fields = "__all__"


class ChooseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseList
        fields = "__all__"
