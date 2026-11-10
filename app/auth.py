"""Small authentication-related validation example."""
import re


def validate_username(username: str) -> bool:
    """Accept usernames with 3–20 ASCII letters, digits, or underscores."""
    return isinstance(username, str) and re.fullmatch(r"[A-Za-z0-9_]{2,20}", username) is not None
