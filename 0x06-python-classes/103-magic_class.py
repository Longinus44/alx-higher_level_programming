#!/usr/bin/python3

import math
"""
A magical class for performing calculations on a given radius.

    Attributes:
    __radius (float): The radius for calculations.
"""
class MagicClass:
    """ represent class magicclass"""
   

    def __init__(self, radius):
        """ 
        Initializes the MagicClass instance with a given radius.

        Args:
        radius (int or float): The radius for calculations.

        Raises:
        TypeError: If the radius is not of type int or float.
        """
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area based on the radius.

        Returns:
        float: The calculated area.
        """
        return 2 ** self.__radius * math.pi

    def circumference(self):

        """
        Calculates and returns the circumference based on the radius.

        Returns:
        float: The calculated circumference.
        """
        return 2 * math.pi * self.__radius
