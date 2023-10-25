#!/usr/bin/python3
"""create a class called node for singly"""


class Node:
    """class node body"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve/get current size"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
         if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """class singlylinkedlined"""


    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Args:
            add(Node): new node
        """
        add = None(value)
        if self.__head is None:
            self.__head = add
        elif self.__head.data > value:
            add.next_node = self.__head
            self.__head = add
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            add.next_node = temp.next_node
            temp.next_node = add

    def __str__(self):
        """print() representation of singlylinkedlist"""
        results = []
        temp = self.head
        while temp:
            results.append(str(temp.data))
            temp = temp.next_node
            return ("\n").join(results)
