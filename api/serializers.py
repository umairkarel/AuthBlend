"""API Serializers"""

from django.contrib.auth.models import User
from rest_framework import serializers
from backend.models import AppUser


class AppUserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating the AppUser model.
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta Properties"""

        model = AppUser
        fields = ["id", "name", "username", "email"]


class AppUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the AppUser model. It is used to create and update AppUser instances.
    """

    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    name = serializers.CharField(required=False)

    def create(self, validated_data):

        if User.objects.filter(username=validated_data["email"]).exists():
            raise serializers.ValidationError("User with Email Already exists.")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        app_user = AppUser.objects.create(
            user=user,
            username=validated_data.get("username"),
            name=validated_data.get("name", ""),
            email=validated_data.get("email"),
        )

        return app_user

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta Properties"""

        model = AppUser
        fields = ["id", "name", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
