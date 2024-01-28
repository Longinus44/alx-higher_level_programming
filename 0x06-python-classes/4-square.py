#!/usr/bin/python3

"""
Square Module:

This module defines the Square class.

Attributes:
    None.

Classes:
    Square: Represents a square with a size attribute.

"""

class Square:
    """represent class square"""

    def __init__(self, size=0):
        """
        initailizing a square
        args:size(int) 
        """
        self.__size = size
    @property
    def size(self):
        """
        Getter method for retrieving the size of square
        returns: int - size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter method for setting size of square
        parameters:
            value (int): the size to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """
        Public Method for calculating area of the square

        returns:
            int: The area of the square 
        """
        
        return self.__size ** 2
    
