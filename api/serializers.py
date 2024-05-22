"""API Serializers"""

from rest_framework import serializers
from backend.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.

    This serializer is used to serialize/deserialize User model.
    """

    password = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
        help_text="Password input should be in plain text.",
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Meta properties for UserSerializer.
        """

        model = User
        fields = ["id", "name", "username", "email", "password"]
