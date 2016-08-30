__author__ = 'naresh'

from linkLists.single_linked_list import Node


class Stack:
    def __init__(self, data=None):
        self.head = None
        if data is not None:
            self.push(data)

    def push(self, data):
        test = Node(data)
        test.set_next(self.head)
        self.head = test

    def pop(self):
        if self.head is None:
            raise IndexError
        else:
            temp = self.head.get_data()
            self.head = self.head.get_next()
            return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        else:
            return self.head.get_data()

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
