#!/usr/bin/python3
"""Module 3-square with the class Square that defines a square,
   including a method to calculate its area."""


class Square:
    """Class Square that defines a square.

    Attributes:
        __size (int): The size of a side of the square.
    """
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
