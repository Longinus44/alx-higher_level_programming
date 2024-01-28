#!/usr/bin/python3

""" 
This module defines the Square class.
Attributes:
    size.
"""
class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    """


    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than or  0")
        self.__size = size