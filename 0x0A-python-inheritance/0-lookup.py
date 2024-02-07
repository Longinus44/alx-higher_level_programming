#!/usr/bin/python3
"""This module 
    Returns a list of object attributes"""

def lookup(obj):
    """
    Parameters:
        obj: The object whose attributes and methods are to be listed.

    Returns:
        list: A list of available attributes and methods of the object.
    
    """

    return dir(obj) 
