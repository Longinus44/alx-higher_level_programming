#!/usr/bin/python3

""" This module defines a Rectangle class"""

class Rectangle:
    """represents class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ 
            initialise class;
            parameters:
                width and height
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height) 
    
    def __str__(self) -> str:
        """  
        If either width or height is equal to 0, an empty string is returned.
        The rectangle is represented by repeating '#' characters in the specified format.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += str(Rectangle.number_of_instances) * self.__width + "\n"
        return rectangle_str.rstrip()
    
    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreating an instance using eval().

        Returns:
            str: String representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        """
            when an instance of Rectangle is deleted, it will print the message "Bye rectangle.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
