__author__ = 'naresh'

# Algo to find lowest common ansestor of binary tree and BST

from bst import TreeNode


def findLowestAnsestor(root, n1, n2):
    if root is None:
        return None
    else:
        if root.data == n1 or root.data == n2:
            return root

        left = findLowestAnsestor(root.left, n1, n2)
        right = findLowestAnsestor(root.right, n1, n2)
        if left and right:
            return root
        if left:
            return left
        elif right:
            return right
        return None


def findLowestAnsestorBST(root, n1, n2):
    if root is None:
        return None
    else:
        if root.data > n1 and root.data > n2:
            findLowestAnsestorBST(root.left, n1, n2)
        elif root.data < n1 and root.data < n2:
            findLowestAnsestor(root.right, n1, n2)
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print "LCA(4, 5) = ", findLowestAnsestor(root, 4, 5)
    print "LCA(4, 6) = ", findLowestAnsestor(root, 4, 6)
    print "LCA(3, 4) = ", findLowestAnsestor(root, 3, 4)
    print "LCA(2, 4) = ", findLowestAnsestor(root, 2, 4)
