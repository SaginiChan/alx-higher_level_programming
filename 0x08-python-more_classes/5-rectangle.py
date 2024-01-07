#!/usr/bin/python3
"""This defines a rectangle"""


class Rectangle:
    """A rectangle representation"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width should be an integer")
        if value < 0:
            raise ValueError("width should be >= 0")
        self.__width = value

    @property
    def height(self):
        """Define height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be an integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value

    def area(self):
        """This  returns the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """This returns printable version of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for c in range(self.__height):
            [rect.append('#') for b in range(self.__width)]
            if c != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """This returns string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Prints notification for every deleted rectangle"""
        print("Gone so soon...")
