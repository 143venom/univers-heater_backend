from .models import *
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "password",
        )
        

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "address",
        )