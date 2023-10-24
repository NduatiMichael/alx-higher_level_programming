#!/usr/bin/python3
"""
This module defines a Singly linked list
"""


class Node:
    """
    Defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with the given data and next_node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node to the given value.
        Raises a TypeError exception if the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the next node of the list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node of the list to the given value.
        Raises a TypeError exception if the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty SinglyLinkedList object.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).
        """
        new_node = Node(value)

        # if the list is empty or the new node is smaller than the head
        if self.head is None or new_node.data < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            # find the right position to insert the new node
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
