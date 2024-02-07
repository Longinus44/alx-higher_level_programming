#!/usr/bin/python3

"""   Checks if an object is an exact instance of the specified class."""

def is_same_class(obj, a_class):
	"""
   	Args:
       		obj: The object to check.
       		a_class: The class to compare against.

   	Returns:
       		True if the object is an exact instance of the class, False otherwise.
   	"""
	return type(obj) is a_class
