#!/usr/bin/python3

"""
define class Square
returns the current square area
"""

class Square:
    """class Square"""

    def __init__(self, size=0):
        """initailizes a Square.
        args:
        size(int):the size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Return the current area of square"""
        return self.__size ** 2
