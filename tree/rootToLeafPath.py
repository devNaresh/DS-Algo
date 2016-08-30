__author__ = 'naresh'

# Algo to print all paths from root node to all its leaf
from bst import create_tree


def printPaths(root, arr):
    if root is None:
        print arr
        return
    else:
        arr.append(root.get_data())
        printPaths(root.get_left(), arr)
        if root.get_right():
            printPaths(root.get_right(), arr)
    arr.pop()


if __name__ == "__main__":
    arr = [32, 4, 5, 75, 904, 75, 1, 5, 667, 13, 76]
    tree = create_tree(arr)
    printPaths(tree.root, [])

