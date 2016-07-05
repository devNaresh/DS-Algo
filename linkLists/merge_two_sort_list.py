from __future__ import print_function

__author__ = 'naresh'

from single_linked_list import Node, LinkedList


def merge(l1, l2):
    main_node = Node(0)
    node = main_node

    while l1 is not None and l2 is not None:
        if l2.get_data() <= l1.get_data():
            node.set_next(Node(l1.get_data()))
            node = node.get_next()
            l1 = l1.get_next()
        elif l1.get_data() <= l2.get_data():
            node.set_next(Node(l2.get_data()))
            node = node.get_next()
            l2 = l2.get_next()
    if l1 is None:
        node.set_next(l2)
    else:
        node.set_next(l1)
    return main_node.get_next()

if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()

    l1.create_list([40, 30, 15, 5])
    l2.create_list([45, 40, 10])

    out = merge(l1.head, l2.head)

    while out is not None:
        print(out.get_data(), end=' ')
        out = out.get_next()
