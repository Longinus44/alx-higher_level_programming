#!/usr/bin/python3

""" This module defines a Rectangle class"""

class Rectangle:
    """represents class Rectangle"""
    def __init__(self, width=0, height=0):
        """ 
            initialise class;
            parameters:
                width and height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method for retrieval"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """ Setter method for setting value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height retrieval"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter method for setting height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0 :
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area """
        return self.__width * self.__height
        
    def perimeter(self):
        """ return the perimeter"""
        return 2 * (self.__width + self.__height) 
    
    