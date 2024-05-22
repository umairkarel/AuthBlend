"""URL configuration for API App."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import AppUserViewSet

router = DefaultRouter()
router.register("users", AppUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
