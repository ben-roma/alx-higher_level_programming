#!/usr/bin/python3
"""
Module 10-square.
Extends the Rectangle class from 9-rectangle.py with a Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle and represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance, validating size as a positive integer.

        Args:
            size (int): The size of the sides of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the square description.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
