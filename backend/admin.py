"""Admin Accessible Models"""

from django.contrib import admin
from backend.models import AppUser

# Register your models here.

admin.site.register(AppUser)
