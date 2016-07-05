__author__ = 'naresh'

## Algo to search an element in binary tree

from bst import create_tree


def search(root, data):
    if root is None:
        return root
    else:
        if root.get_data() == data:
            return root
        else:
            node = search(root.get_left(), data)
            if node is not None:
                return node
            else:
                return search(root.get_right(), data)


if __name__ == "__main__":
    arr = [32, 4, 5, 75, 904, 75, 1, 5, 667, 13, 76]
    tree = create_tree(arr)
    node = search(tree.root, 34)
    if node is not None:
        print "Node Found"
    else:
        print "Node not found"
