from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'me', LoggedInUser, basename='logged_in_user')


urlpatterns = [
    path('', include(router.urls)),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
]