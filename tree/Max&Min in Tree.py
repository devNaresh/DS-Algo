__author__ = 'naresh'

## Algo to find max and min element in Tree

from bst import create_tree

max_num = 0
min_num = None


def find_max(root):
    global max_num

    if root is None:
        return 0

    else:
        if root.get_data() > max_num:
            max_num = root.get_data()

        find_max(root.get_left())
        find_max(root.get_right())


def find_min(root):
    global min_num

    if root is None:
        return 0
    else:
        if min_num is None:
            min_num = root.get_data()

        elif root.get_data() < min_num:
            min_num = root.get_data()

        find_min(root.get_left())
        find_min(root.get_right())


if __name__ == "__main__":
    arr = [32, 4, 5, 75, 904, 75, 1, 5, 667, 13, 76]
    tree = create_tree(arr)
    find_max(tree.root)
    find_min(tree.root)
    print max_num
    print min_num
