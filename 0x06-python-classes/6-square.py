#!/usr/bin/python3
"""Module 6-square with the class Square that defines a square,
   including a position attribute and modifying the print method."""


class Square:
    """Class Square that defines a square.

    Attributes:
        __size (int): The size of a side of the square.
        __position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of a side of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of a side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: The position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.size * self.size

    def my_print(self):
        """Print square with the character '#', considering its position."""
        if self.size == 0:
            print("")
            return
        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
