#!/usr/bin/python3

"""
This module defines class Node
Attribute:
    data
"""

class Node:
    """represents class Node"""

    def __init__(self, data, next_node = None):
        """initialises the Node class
            parameters:
                data and next_node
        """
        self._data = data
        self._next_node = next_node


    @property
    def data(self):
        """
        Getter method to retrieve the data
        """
        return self._data
    
    @data.setter
    def data(self, value):
        """
        Setter method to set data value
        Raises:
            Typeerror if data is not an interger
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieval
        """
        return self._next_node
    
    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set value
        Raises:
            Typeerror if data is not an interger
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value

"""This module defines a SinglyLinkedList class"""
class SinglyLinkedList:
    """represents class SinglyLinkedList"""

    def __init__(self):
        """ instantiates class SinglyLinkedList"""
        self.head = None

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted position """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value > current.next_node.data:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)





