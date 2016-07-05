__author__ = 'naresh'

from bst import Tree

from stack.stack import Stack
# Algo to find path b/w two nodes of BST

def findLCA(root, n1, n2):
    if root is None:
        return None
    else:
        if n1 == root.data or n2 == root.data:
            return root

        left = findLCA(root.left, n1, n2)
        right = findLCA(root.right, n1, n2)
        if left and right:
            return root
        if left:
            return left
        elif right:
            return right
        return None


def findLCABST(root, n1, n2):
    if root is None:
        return None
    else:
        if n1 < root.data and n2 < root.data:
            findLCABST(root.left, n1, n2)
        elif n1 > root.data and n2 > root.data:
            findLCABST(root.left, n1, n2)
        return root


# def findPath(root, n1, n2, arr):
#     lca = findLCABST(root, n1, n2)
#     s1 = Stack()
#     s2 = Stack()
#     if lca.data == n1:
#         s1.push(n1)
#     elif lca.data == n2:
#         s1.push(n2)






if __name__ == '__main__':
    arr = [15, 10, 20, 5, 17, 25, 1, 7, 8]
    tree = Tree()
    tree.create_bst(arr)
    Tree.print_inorder(tree.root)
    print "\n"
    arr = []
    findPath(tree.root, 1, 17, arr)
    print arr
