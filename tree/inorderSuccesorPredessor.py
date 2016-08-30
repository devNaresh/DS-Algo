__author__ = 'naresh'

# Algo to find Inorder Succesor and Predessor BST

from bst import Tree


def findMin(node):
    while node.get_left(): node = node.get_left()
    return node


def findMax(node):
    while node.get_right(): node = node.get_right()
    return node


def finInorderSuccessor(root, data):
    current_ptr = None
    if root is None:
        return None

    while data != root.get_data():
        if data < root.get_data():
            current_ptr = root
            root = root.get_left()
        else:
            root = root.get_right()

    if root.get_right() is not None:
        current_ptr = findMin(root.get_right())

    return current_ptr


def finInorderPredessor(root, data):
    current_ptr = None
    if root is None:
        return None

    while data != root.get_data():
        if data < root.get_data():
            root = root.get_left()
        else:
            current_ptr = root
            root = root.get_right()

    if root.get_left() is not None:
        current_ptr = findMax(root.get_left())

    return current_ptr


if __name__ == '__main__':
    arr = [15, 10, 20, 5, 17, 25, 1, 7, 8]
    tree = Tree()
    tree.create_bst(arr)
    Tree.print_inorder(tree.root)
    ptr = finInorderPredessor(tree.root, 25)
    print "\n"
    print ptr.data
