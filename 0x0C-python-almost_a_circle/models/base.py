#!/usr/bin/python3

"""This module defines a Base class"""


import json


class Base:
    """
    attributes:
        id - a parameter that the base class accepts
    """
    __nb_object = 0

    def __init__(self, id=None):
        """initialises the class with attribute id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)
