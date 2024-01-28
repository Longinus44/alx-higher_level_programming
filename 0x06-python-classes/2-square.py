#!/usr/bin/python3

#!/usr/bin/python3

""" 
This module defines the Square class.
Attributes:
    size.
"""
class Square:
    """
    Attributes:
        size (int): The size of the square.
    """


    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        