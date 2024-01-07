#!/usr/bin/python3
"""This script defines a class called Rectangle that represents a rectangle."""

class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0.")
        self._width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0.")
        self._height = value

    def area(self):
        """Return the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Return the printable representation of the rectangle.

        Represents the rectangle with the # character.
        """
        if self._width == 0 or self._height == 0:
            return ""

        rect = []
        for i in range(self._height):
            [rect.append("#") for j in range(self._width)]
            if i != self._height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return the string representation of the rectangle."""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Print a message for every deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
