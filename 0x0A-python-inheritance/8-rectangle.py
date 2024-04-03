#!/usr/bin/python3
"""
Module 8-rectangle.
Defines a class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry. Implements a Rectangle with width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance, validating width
        and height as positive integers.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
