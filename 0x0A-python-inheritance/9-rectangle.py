#!/usr/bin/python3
"""
Module 9-rectangle.
Extends the BaseGeometry class from 7-base_geometry.py with a class Rectangle
that adds an implementation of area() and customizes str().
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry and implements a Rectangle.
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

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
