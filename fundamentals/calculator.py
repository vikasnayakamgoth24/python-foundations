"""Basic arithmetic operations with input validation."""


def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Return the difference between two numbers."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Return the product of two numbers."""
    return first * second


def divide(first: float, second: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If the divisor is zero.
    """
    if second == 0:
        raise ValueError("Division by zero is not allowed.")

    return first / second