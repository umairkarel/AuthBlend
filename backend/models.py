"""All the Backend Models"""

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AppUser(models.Model):
    """AppUser Entity Model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="myuser")
    username = models.CharField(max_length=30, unique=True)
    name: str = models.CharField(max_length=30, blank=True)
    email: str = models.EmailField()
    joined_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
