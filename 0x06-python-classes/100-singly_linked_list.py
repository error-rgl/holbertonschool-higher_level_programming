#!/usr/bin/python3
"""Class defines a node
"""


class Node:
    """ defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter for data attribute"""
        return(self.__data)

    @data.setter
    def data(self, value):
        """setter for data attribute"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Method to returns the nex_node value.
        """
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Method to set the next_node value of the Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """defines class for singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """insert new node"""
        new_nod = Node(value)

        if not self.__head or self.__head.data >= value:
            new_nod.next_node = self.__head
            self.__head = new_nod

        else:
            tmp = self.__head
            while (tmp.next_node and (tmp.next_node).data < value):
                tmp = tmp.next_node

            new_nod.next_node = tmp.next_node
            tmp.next_node = new_nod

    def __str__(self):
        tmp = self.__head
        lis = []
        while tmp is not None:
            lis.append(tmp.data)
            tmp = tmp.next_node
        StrA = "\n".join(map(str, lis))
        return(StrA)
