"""All the Backend Models"""

from django.db import models
from django.utils import timezone
from backend.validators import (  # pylint: disable=E0611
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
        # Update the 'updated_at' field whenever the record is saved.
        self.updated_at = timezone.now()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
