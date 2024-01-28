#!/usr/bin/python3

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
    """Representd class square"""

    def __init__(self, size=0,position = (0,0)):
        """
        initialise a new instatance of square class
        parameters:
            size(int) - the size of the square
        """
        self.__size = size
        self.__Position = position

    @property
    def size(self):
        """
        Getter - to retrieve the square size
        Returns:
            int: the size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter method -  set the size of the square
         Parameters:
            value (int): The size to be set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method - retrieves the square size

        """
        return self.__Position
    
    @position.setter
    def position(self, value):
        """
        Setter method -  set the size of the square
         Parameters:
            value (int): The size to be set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(value, int) and val >=0 for val in value): 
            raise TypeError("position must be a tuple of positive integers")
        self.position = value

    def area(self):
        """
        Public method for calculating the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Public methiod that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__Position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__Position[0] + "#" * self.__size)
                