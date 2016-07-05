from __future__ import print_function

__author__ = 'naresh'


class Node:
    def __init__(self, data=None):
        self.data = data
        self._next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

    def has_next(self):
        return self._next is not None

    def __getitem__(self, item):
        return self.data

    def __str__(self):
        return self.data


class LinkedList(object):
    def __init__(self, node=None):
        self.head = node
        self.length = 0

    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.length = self.length + 1
            return

        elif node.data < self.head.data:
            self.add_beg(node)
            return

        current_node = self.head

        while current_node._next is not None and current_node._next.data < node.data:
            current_node = current_node._next
        if current_node._next is not None:
            node._next = current_node._next
            current_node._next = node
            self.length = self.length + 1
            return

        elif current_node._next is None:
            current_node._next = node
            self.length = self.length + 1
            return

    def add_beg(self, node):
        node._next = self.head
        self.head = node
        self.length = self.length + 1
        return

    def __iter__(self):
        current_node = self.head
        while True:
            if current_node is None:
                raise StopIteration
            yield current_node.data
            current_node = current_node._next
            # LinkListIter(self.head)

    def reverse_list(self):
        prev_node = None
        current = self.head
        next_node = None

        while current != None:
            next_node = current.get_next()
            current.set_next(prev_node)
            prev_node = current
            current = next_node

        self.head = prev_node

    def reverseKBlock(self, head, k):
        temp = Node(0)
        temp.set_next(head)
        previous = temp
        while True:
            begin = previous.get_next()
            end = previous
            for i in range(0, k):
                end = end.get_next()
                if end == None:
                    return temp.get_next()
            nextBlock = end.get_next()
            self.reverseList(begin, nextBlock)
            previous.set_next(end)
            begin.set_next(nextBlock)
            previous = begin

    def reverseList(self, start, end):
        current = start
        prev = None
        next = None
        while current != end:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        return prev

    def print_data(self, head):
        while head is not None:
            print(head.get_data(), end=' ')
            head = head.get_next()

    def create_list(self, data):
        start = self.head
        for x in data:
            if start is None:
                start = Node(x)
                self.head = start
            else:
                start.set_next(Node(x))
                start = start.get_next()


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)

    l1 = LinkedList()
    l1.add_node(n1)
    l1.add_node(n2)
    l1.add_node(n3)
    l1.add_node(n4)
    l1.add_node(n5)
    l1.add_node(n6)
    l1.add_node(n7)
    l1.add_node(n8)

    for x in l1:
        print(x, end=' ')

    head = l1.reverseKBlock(l1.head, 4)

    print('\n')

    l1.print_data(head)
