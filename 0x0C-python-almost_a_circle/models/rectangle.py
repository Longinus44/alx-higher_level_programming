#!/usr/bin/python3
from .base import Base

"""This module define class rectangle that ingerits from class Base"""


class Rectangle(Base):
    """The class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises the class with the attributes """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = 0

        @property
        def width(self):
            """this defines a getter method for width"""
            return self.width

        @width.setter
        def width(self, value):
            """defines a setter method for width"""
            self.width = value

        @property
        def height(self):
            """this defines a getter method for height"""
            return self.height

        @height.setter
        def height(self, value):
            """defines a setter method for height"""
            self.height = value

        @property
        def x(self):
            """this defines a getter method for x"""
            return self.x

        @x.setter
        def x(self, value):
            """defines a setter method for x"""
            self.x = value

        @property
        def y(self):
            """this defines a getter method for width"""
            return self.y

        @y.setter
        def y(self, value):
            """defines a setter method for y"""
            self.y = value
