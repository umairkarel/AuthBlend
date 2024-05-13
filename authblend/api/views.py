"""API Views"""

from backend.models import User
from api.serializers import UserSerializer
from rest_framework import viewsets

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer
