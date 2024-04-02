#!/usr/bin/python3
"""Module 9-rectangle
Defines a class Rectangle with a class method to create squares.
"""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the printable representation of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return ""

        rect_lines = [str(self.print_symbol) * self.width
                      for _ in range(self.height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Detects instance deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle) or not isinstance(rect_2,
                                                               Rectangle):
            raise TypeError("rect_1 and rect_2 must be instances of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the sides of the square.

        Returns:
            A new Rectangle instance where width == height == size.
        """
        return cls(size, size)
