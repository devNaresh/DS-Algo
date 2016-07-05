__author__ = 'naresh'


# Algo to delete node from BST

# Here Three cases needs to be consider for that
#     1. Node with no child
#     2. Node with one child
#     3. Node with both child

def delete(root, data):
    if root is None:
        return None
    else:
        if data < root.data:
            root.left = delete(root.left, data)
        elif data > root.data:
            root.right = delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            node = findMin(root.right)
            root.data = node.data
            root.right = delete(root.right, root.data)
        return root


def findMin(root):
    current = root
    while current.left is not None:
        current = current.left
    return current
