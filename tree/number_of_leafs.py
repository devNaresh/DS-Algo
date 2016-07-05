__author__ = 'naresh'

## Algo to find number of leafs in a tree
from bst import create_tree
from queues.queue import Queue


def find_leafs(root):
    count = 0
    queue = Queue()
    if root is not None:
        queue.enQueue(root)

    while not queue.isEmpty():
        node = queue.deQueue()

        if node.get_left() is None or node.get_right() is None:
            count += 1

        if node.get_left() is not None:
            queue.enQueue(node.get_left())

        if node.get_right() is not None:
            queue.enQueue(node.get_right())

    return count

if __name__ == "__main__":
    arr = [32, 4, 5, 75, 904, 75, 1, 5, 667, 13, 76, 56]
    tree = create_tree(arr)
    print find_leafs(tree.root)
