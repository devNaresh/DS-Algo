from __future__ import print_function

__author__ = 'naresh'

from queues.queue import Queue


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def set_right(self, node):
        self.right = node

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, data=None):
        if data:
            self.root = TreeNode(data)
        else:
            self.root = None

    def add_left(self, node):
        if self.root is None:
            self.root = node
        else:
            self.left = node

    def add_right(self, node):
        if self.root is None:
            self.root = node
        else:
            self.right = node

    def add_array(self, i, array):
        temp = TreeNode()
        if (i < len(array)):
            temp.data = array[i]
            temp.left = self.add_array(2 * i + 1, array)
            temp.right = self.add_array(2 * i + 2, array)
            return temp
        else:
            return None

    def insert_element(self, data):
        new_node = TreeNode(data)

        queue = Queue()
        queue.enQueue(self.root)

        while not queue.isEmpty():
            node = queue.deQueue()
            if node.get_left() is None:
                node.set_left(new_node)
                break
            else:
                queue.enQueue(node.get_left())

            if node.get_right() is None:
                node.set_right(new_node)
                break
            else:
                queue.enQueue(node.get_right())

    def insert_bst(self, root, data):
        new_node = TreeNode(data)
        if self.root is None and root is None:
            self.root = new_node
            root = self.root
        else:
            if data < root.get_data():
                if root.get_left() is None:
                    root.left = new_node
                else:
                    self.insert_bst(root.get_left(), data)
            else:
                if root.get_right() is None:
                    root.right = new_node
                else:
                    self.insert_bst(root.get_right(), data)

    def print_level_order(self):
        queue = Queue()
        queue.enQueue(self.root)

        while not queue.isEmpty():
            node = queue.deQueue()
            print(node.data, end=",")
            if node.left:
                queue.enQueue(node.left)
            if node.right:
                queue.enQueue(node.right)
        print("\n")

    @staticmethod
    def print_inorder(root):
        if root is None:
            return 0
        Tree.print_inorder(root.get_left())
        print(root.data, end=',')
        Tree.print_inorder(root.get_right())

    def create_bst(self, arr):
        for x in arr:
            self.insert_bst(self.root, x)
        return self

    @staticmethod
    def get_size(root):
        if root is None:
            return 0
        else:
            return Tree.get_size(root.get_left()) + Tree.get_size(root.get_right()) + 1


def create_tree(arr):
    tree = Tree()
    tree.root = tree.add_array(0, arr)
    return tree


if __name__ == "__main__":
    temp = [2, 3, 3, 5, 45, 4, 6, 5, 67, 7]
    tree = Tree()
    tree.root = tree.add_array(0, temp)
    print("Before Adding new element")
    tree.print_level_order()

    tree.insert_element(903)
    print("After Adding new element")
    tree.print_level_order()

    print(tree.get_size(tree.root))
