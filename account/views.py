from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import CustomUser
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets

@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=email, password=password)
    if user is None:
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    user_serializer = UserDetailsSerializer(user)
    
    return Response({"token": token.key, "user": user_serializer.data}, status=status.HTTP_200_OK)

@api_view(["POST"])
def register(request):
    serializer = UserCreateSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": "User created!", "user_id": user.id}, status=status.HTTP_201_CREATED)
    
    return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token = request.auth
        token.delete()
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({"error": "Token not found."}, status=status.HTTP_404_NOT_FOUND)
    
class LoggedInUser(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
