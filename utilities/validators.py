"""Reusable validation utilities."""

import re


def is_valid_email(email: str) -> bool:
    """Return True if the email has a valid basic structure."""
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.fullmatch(pattern, email) is not None


def is_valid_phone(phone: str) -> bool:
    """Return True if the phone contains exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10


def is_valid_positive_number(value: float) -> bool:
    """Return True if the value is greater than zero."""
    return value > 0