"""API Views"""

from rest_framework import viewsets
from backend.models import AppUser
from api.serializers import AppUserSerializer, AppUserUpdateSerializer

# Create your views here.


class AppUserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = AppUser.objects.all().order_by("-joined_on")
    serializer_class = AppUserSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return AppUserUpdateSerializer
        return AppUserSerializer
