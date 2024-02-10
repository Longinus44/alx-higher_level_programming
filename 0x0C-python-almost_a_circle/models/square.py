#!/usr/bin/python3
from .rectangle import Rectangle

""" This module defines Square class"""


class Square(Rectangle):
    """ represents class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width if hasattr(self, "width") else self.height)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square attributes"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == 'size':
                    self.width = value
                    self.height = value

        def to_dictionary(self):
            """Return dictionary representation of the square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "Y": self.y
        }
