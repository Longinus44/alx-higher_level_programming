#!/usr/bin/python3

"""This module creates a class MyList that returns a sorted list"""

class MyList(list):
	"""
    		A custom list class inheriting from the built-in list class.
    	"""
	
	def print_sorted(self):
		"""
		Returns:
            		list: A sorted version of the list.
        	"""
		print(sorted(self))
