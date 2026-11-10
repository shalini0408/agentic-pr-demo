"""Small authentication-related validation example."""
import re


def validate_username(username: str) -> bool:
    """Accept usernames with 3–20 ASCII letters, digits, or underscores
    Validate password strength.
    """
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    return True