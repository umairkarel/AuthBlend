"""Backend Apps"""

from django.apps import AppConfig


class BackendConfig(AppConfig):
    """App Config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend"
