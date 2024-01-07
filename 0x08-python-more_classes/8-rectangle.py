#!/usr/bin/python3
"""This script defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Return the printable representation of the rectangle.

        Represents the rectangle with the specified print_symbol character.
        """
        if self._width == 0 or self._height == 0:
            return ""
        rect = []
        for i in range(self._height):
            [rect.append(str(self.print_symbol)) for j in range(self._width)]
            if i != self._height - 1:
                rect.append("\n")
                return "".join(rect)

    def __repr__(self):
        """Return the string representation of the rectangle."""
        return

    def __del__(self):
        """Print a message for every deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")