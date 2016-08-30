__author__ = '__naresh__'

# WAP to Reverse Block of K in Link List


from single_linked_list import LinkedList


def reverse_list(start, end):
    prev = None
    current = start
    next_node = None

    while current != end:
        next_node = current.get_next()
        current.set_next(prev)
        prev = current
        current = next_node

    return prev


def reverse_block(head, k):
    start = end = pointer = head
    temp = 0

    while end is not None:
        if temp == k:
            if start == head:
                head = reverse_list(start, end)
                pointer = start
            else:
                pointer.set_next(reverse_list(start, end))
                pointer = start
            start = end
            temp = 0
        temp += 1
        end = end.get_next()
    return head


if __name__ == "__main__":
    l1 = LinkedList()
    l1.create_list([40, 35, 30, 25, 20, 15, 10, 5, 1, 2, 75, 85])

    l1.head = reverse_block(l1.head, 2)
    l1.print_data(l1.head)
