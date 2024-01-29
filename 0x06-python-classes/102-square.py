#!/usr/bin/python

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
    
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        result = ""
        for _ in range(self.position[1]):
            result += "\n"
        for _ in range(self.size):
            result += " " * self.position[0] + "#" * self.size + "\n"
        return result.rstrip()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
    