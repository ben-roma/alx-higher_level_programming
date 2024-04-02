#!/usr/bin/python3
"""Module 3-rectangle
Defines a class Rectangle with properties width and height, and
methods to calculate the area, perimeter, and a string representation.
"""


class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle.

        Returns:
            0 if either the width or the height is 0.
            Otherwise, returns the calculated perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the printable representation of the Rectangle.

        Represents the rectangle with the character # for each position.
        Returns an empty string if the width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rect = []
        for i in range(self.height):
            rect.append("#" * self.width)
        return "\n".join(rect)
