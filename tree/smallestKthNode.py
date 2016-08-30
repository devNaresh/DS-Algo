__author__ = 'naresh'

# Algo to find smallest Kth Node in BST
from bst import Tree

count = 0


def findSmallest(root, kth):
    global count
    if root is None:
        return None
    else:
        left = findSmallest(root.left, kth)
        if left:
            return left
        if count == kth:
            return root
        count += 1
        return findSmallest(root.right, kth)


if __name__ == '__main__':
    arr = [15, 10, 20, 5, 17, 25, 1, 7, 8]
    tree = Tree()
    tree.create_bst(arr)
    Tree.print_inorder(tree.root)
    print "\n"
    for k in range(5):
        count = 0
        print findSmallest(tree.root, k)
