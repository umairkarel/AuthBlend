"""All the Backend Models"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from backend.validators import (
    validate_username,
    validate_password,
)


# Create your models here.
class User(models.Model):
    """User Entity Model"""

    name: str = models.CharField(max_length=30, blank=True)
    username: str = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True,
        validators=[validate_username],
    )
    password: str = models.CharField(
        max_length=15, blank=False, null=False, validators=[validate_password]
    )
    email: str = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Save the user object to the database.

        Parameters:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        self.password = make_password(self.password)
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
