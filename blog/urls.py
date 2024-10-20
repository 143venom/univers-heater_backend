from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'blogs', BlogViewSet)
router.register(r'blogs/(?P<blog_pk>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]