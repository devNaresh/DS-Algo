__author__ = 'naresh'

# Algo to find max path sum of binary tree
from bst import create_tree
from bst import TreeNode, Tree

maxPathSum = 0


def findMaxPathSum(root):
    global maxPathSum
    if root is None:
        return 0
    else:
        ls = findMaxPathSum(root.get_left())
        rs = findMaxPathSum(root.get_right())
        current_sum = max(ls + rs + root.get_data(), max(ls, rs))
        if current_sum > maxPathSum:
            maxPathSum = current_sum
        return max(ls, rs) + root.data


if __name__ == "__main__":
    arr = [32, 4, 5, 75, 904, 75, 1, 5, 667, 13, 76, 56]
    tree = create_tree(arr)

    # root = TreeNode(-5)
    # root.left = TreeNode(1)
    # root.right = TreeNode(4)
    # root.left.left = TreeNode(-6)
    # root.left.right = TreeNode(5)
    # root.left.right.left = TreeNode(-2)
    # root.left.right.right = TreeNode(3)
    # root.left.left.left = TreeNode(9)
    # root.left.left.right = TreeNode(10)
    # root.right.left = TreeNode(11)
    # root.right.right = TreeNode(-2)
    # root.right.right.right = TreeNode(-8)
    # root.right.right.left = TreeNode(7)
    # root.right.right.right.left = TreeNode(1)
    # root.right.right.right.right = TreeNode(7)
    # root.right.right.right.right.left = TreeNode(12)
    # tree = Tree()
    # tree.root = root
    findMaxPathSum(tree.root)
    print maxPathSum
