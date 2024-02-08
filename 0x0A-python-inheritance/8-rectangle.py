#!/usr/bin/python3
from .7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
            Initialize the rectangle with width and height.

            Args:
             width (int): The width of the rectangle.
                    height (int): The height of the rectangle.

            Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are less than or equal to 0.
    """

    def __init__(self, width, height):
        super().__init__()
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
