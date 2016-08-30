__author__ = 'naresh'

from bst import create_tree


def findDiameter(root):
    if root is None:
        return 0
    else:
        hl = findHeight(root.get_left())
        hr = findHeight(root.get_right())

        tl = findDiameter(root.get_left())
        tr = findDiameter(root.get_right())

        return max(max(tl, tr), hl + hr + 1)


def findHeight(root):
    if root is None:
        return 0
    else:
        return 1 + max(findHeight(root.get_left()), findHeight(root.get_right()))


if __name__ == "__main__":
    arr = [32, 4, 5, 75, 904, 75, 1, 5, 667, 13, 76, 56]
    tree = create_tree(arr)
    print findDiameter(tree.root)
