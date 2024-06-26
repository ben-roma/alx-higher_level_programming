#!/usr/bin/python3
"""Module 4-square with the class Square that defines a square,
   including a property and property setter for size to validate its value."""


class Square:
    """Class Square that defines a square.

    Attributes:
        __size (int): The size of a side of the square.
    """
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: The size of a side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of a side of the square.

        Args:
            value (int): The new size of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.size * self.size
