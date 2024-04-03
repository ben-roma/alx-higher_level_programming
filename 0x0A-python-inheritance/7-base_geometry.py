#!/usr/bin/python3
"""
Module 7-base_geometry.
Expands upon 6-base_geometry.py with a method to validate integer value.
"""


class BaseGeometry:
    """A class with methods area and integer_validator not
    yet fully implemented."""

    def area(self):
        """Raises an Exception with the message that
        the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
