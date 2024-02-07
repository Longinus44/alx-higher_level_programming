#!/usr/bin/python3

"""This module define a baseclass and raise an exception error"""

class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Calculate the area.
        
        Raises:
        - Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")
