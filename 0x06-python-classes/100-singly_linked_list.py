#!/usr/bin/python3
"""Define Classes for a singly-linked list"""


class Node:
    """A node"""
    def __init__(self, data, next_node=None):
        """Initialize a new node
        Args:
            Data (int): The data
            Next_node (Node): The next one
        """
        self.data = data
        sel.next_node = next_node

    @property
    def data(self):
        """get/set the data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get/set the next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """a singly linked list"""

    def __init__(self):
        """Initialize a new list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node
        Args:
            value (Node): the new node
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print function"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
