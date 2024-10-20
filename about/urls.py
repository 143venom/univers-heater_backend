# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"about", AboutViewSet, basename="about")
router.register(r"about-list", AboutListViewSet, basename="about-list")
router.register(r"team", TeamViewSet, basename="team")
router.register(r"testimonial", TestimonialViewSet, basename="testimonial")
router.register(r"story", StoryViewSet, basename="story")
router.register(r"journey", JourneyViewSet, basename="journey")
router.register(r"goal", GoalViewSet, basename="goal")
router.register(r"vision", VisionViewSet, basename="vision")

urlpatterns = [
    path("", include(router.urls)),
]
