__author__ = 'naresh'

# Algo to find level of maxium sum
from bst import create_tree
from queues.queue import Queue


def findLevel(root):
    q = Queue()
    q.enQueue(root)
    q.enQueue(None)
    level = levelsum = totalsum = maxlevel = 0

    while not q.isEmpty():
        node = q.deQueue()
        if node is None:
            if levelsum > totalsum:
                totalsum = levelsum
                maxlevel = level
            levelsum = 0
            if not q.isEmpty():
                q.enQueue(None)
                level += 1
        else:
            levelsum += node.get_data()
            if node.get_left() is not None:
                q.enQueue(node.get_left())
            if node.get_right() is not None:
                q.enQueue(node.get_right())

    return maxlevel, totalsum


if __name__ == "__main__":
    arr = [32, 4, 5, 75, 904, 75, 1, 5, 667, 13, 76]
    tree = create_tree(arr)
    print findLevel(tree.root)
