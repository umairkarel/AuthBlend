"""Model Field Validators"""

import re
from django.core.exceptions import ValidationError


def validate_username(value: str) -> [str, ValidationError]:
    """Utility Function For validating username

    Args:
        value (str): value/username to be validated

    Raises:
        ValidationError: invalid username exception

    Returns:
        [str, ValidationError]: value if validated else exception
    """
    pattern: str = r"^[a-zA-Z][a-zA-Z0-9_]*$"

    if re.match(pattern, value):
        return value
    raise ValidationError("Username Doesn't Match the Conditions")


def validate_password(value: str) -> [str, ValidationError]:
    """Utility Function For validating password

    Args:
        value (str): value/password to be validated

    Raises:
        ValidationError: invalid password exception

    Returns:
        [str, ValidationError]: value if validated else exception
    """
    pattern: str = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,15}$"
    )

    if re.match(pattern, value):
        return value
    raise ValidationError("Password Doesn't Match the Condition")
