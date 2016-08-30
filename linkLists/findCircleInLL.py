__author__ = '__naresh__'

## WAP to find Circle in a Link List

"""
---------- Algo -------------

1) Create Two Pointers
2) Move one pointer by one step and another by two steps
3) Once they meet that will be the meeting point.
4) Make slow pointer equl to Head and move fast pointer by one step.
5) Move Both pointers by step by step

 You will find circle

"""

from single_linked_list import LinkedList


def find_circle(head):
    slow_pointer = fast_pointer = head
    fast_pointer = fast_pointer.get_next()
    while fast_pointer != slow_pointer:
        slow_pointer = slow_pointer.get_next()
        fast_pointer = fast_pointer.get_next().get_next()

    slow_pointer = head
    fast_pointer = fast_pointer.get_next()
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.get_next()
        fast_pointer = fast_pointer.get_next()

    return slow_pointer.get_data()


if __name__ == "__main__":
    l1 = LinkedList()

    l1.create_list([40, 35, 30, 25, 20, 15, 10, 5, 1, 2, 75, 85])
    pointer = l1.head
    while pointer.get_next() != None:
        pointer = pointer.get_next()
    pointer.set_next(l1.head._next._next._next._next)
    find_circle(l1.head)
