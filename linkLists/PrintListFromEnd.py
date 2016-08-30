__author__ = '__naresh__'

## WAP to print list from the END

"""
------------ Algo ------------

Simple Just use Recursion. Once End reach start printing data

"""

from single_linked_list import LinkedList


def print_list_from_end(head):
    if head is None:
        return
    print_list_from_end(head.get_next())
    print head.get_data()


if __name__ == "__main__":
    l1 = LinkedList()
    l1.create_list([40, 35, 30, 25, 20, 15, 10, 5, 1, 2, 75, 85])

    print_list_from_end(l1.head)
