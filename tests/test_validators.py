"""Tests for validation utilities."""

from utilities.validators import (
    is_valid_email,
    is_valid_phone,
    is_valid_positive_number,
)


def test_valid_email():
    assert is_valid_email("vikas@example.com") is True


def test_invalid_email():
    assert is_valid_email("invalid-email") is False


def test_valid_phone():
    assert is_valid_phone("9876543210") is True


def test_invalid_phone():
    assert is_valid_phone("12345") is False
    assert is_valid_phone("abcdefghij") is False


def test_positive_number():
    assert is_valid_positive_number(10) is True


def test_zero_is_not_positive():
    assert is_valid_positive_number(0) is False


def test_negative_number_is_not_positive():
    assert is_valid_positive_number(-5) is False