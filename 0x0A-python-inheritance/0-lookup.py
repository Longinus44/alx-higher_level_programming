#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of object attributes
    Parameters:
        obj: The object whose attributes and methods are to be listed.

    Returns:
        list: A list of available attributes and methods of the object.
    
    """

    return dir(obj) 
