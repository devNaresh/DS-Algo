from __future__ import print_function

__author__ = 'naresh'

from single_linked_list import Node, LinkedList


def rearrange(list):
    first = list
    slow = first
    fast = slow
    secound = None
    new_list = LinkedList()
    new_node = None
    flag = True

    while fast.get_next() and fast.get_next().get_next():
        slow = slow.get_next()
        fast = fast.get_next().get_next()

    secound = slow.get_next()
    slow.set_next(None)

    l1 = LinkedList(secound)
    l1.reverse_list()
    secound = l1.head

    while first and secound:
        if new_node is None:
            new_node = Node(first.get_data())
            new_list.head = new_node
            first = first.get_next()
            flag = False

        elif flag is True:
            new_node.set_next(Node(first.get_data()))
            new_node = new_node.get_next()
            first = first.get_next()
            flag = False

        elif flag is False:
            new_node.set_next(Node(secound.get_data()))
            new_node = new_node.get_next()
            secound = secound.get_next()
            flag = True

    if secound is not None:
        new_node.set_next(secound)
    if first is not None:
        new_node.set_next(first)

    return new_list.head

if __name__ == '__main__':
    l1 = LinkedList()

    l1.create_list([40, 35, 30, 25, 20, 15, 10])

    out = rearrange(l1.head)

    while out is not None:
        print(out.get_data(), end=' ')
        out = out.get_next()
