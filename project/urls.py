from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Univers heater API",
        default_version="v1",
        description="Univers heater Company",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=settings.DEVELOPER_EMAIL),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("about.urls")),
    path("api/v1/", include("blog.urls")),
    path("api/v1/", include("company_setting.urls")),
    path("api/v1/", include("contact.urls")),
    path("api/v1/", include("home.urls")),
    path('api/v1/',include('account.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path("api/v1/", include("shop.urls")),
    # path('api/v1/', include('djoser.urls')),
    # path('api/v1/', include('djoser.urls.jwt')),

    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("i18n/", include("django.conf.urls.i18n")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)