#!/usr/bin/python3
from .base import Base

"""This module define class rectangle that ingerits from class Base"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises the class with the attributes """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """this defines a getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """defines a setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """this defines a getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """defines a setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """this defines a getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """defines a setter method for x"""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """this defines a getter method for width"""
        return self.__y

    @y.setter
    def y(self, value):
        """defines a setter method for y"""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """ area method that returns the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """this method prints # in height times"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """the string print format"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, (self.__x), (self.__y), (self.__width), (self.__height)))
