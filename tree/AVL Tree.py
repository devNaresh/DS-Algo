__author__ = '__naresh__'


class TreeNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_height(self):
        return self.height

    def set_left(self, data):
        self.left = TreeNode(data)

    def set_right(self, data):
        self.right = TreeNode(data)

    def set_height(self, height):
        self.height = height


def height(node):
    if node is None:
        return 0
    else:
        return node.height


class AVLTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        newnode = node.right
        node.right = newnode.left
        newnode.left = node

        node.height = max(height(node.left), height(node.right)) + 1
        newnode.height = max(height(newnode.left), height(newnode.right)) + 1
        return newnode

    def right_rotate(self, node):
        newnode = node.left
        node.left = newnode.right
        newnode.right = node

        node.height = max(height(node.left), height(node.right)) + 1
        newnode.height = max(height(newnode.left), height(newnode.right)) + 1
        return newnode

    def _insert(self, node, data):
        if node is None:
            node = TreeNode(data)
            if self.root is None: self.root = node
            return node

        else:
            if data < node.data:
                node.left = self._insert(node.get_left(), data)
            elif data > node.data:
                node.right = self._insert(node.get_right(), data)
        node_height = max(height(node.left), height(node.right)) + 1
        node.set_height(node_height)

        height_diff = height(node.left) - height(node.right)

        ## Left Left Case
        if height_diff > 1 and data < node.data:
            new_node = self.right_rotate(node)
            if node is self.root:
                self.root = new_node
            return new_node

        ## Right Right Case
        if height_diff < -1 and data > node.data:
            new_node = self.left_rotate(node)
            if node is self.root:
                self.root = new_node
            return new_node

        ## Left Right Case:
        if height_diff > 1 and data > node.data:
            node.left = self.left_rotate(node.left)
            new_node = self.right_rotate(node)
            if node is self.root:
                self.root = new_node
            return new_node

        ## Right Left Case:
        if height_diff < -1 and data < node.data:
            node.right = self.right_rotate(node.right)
            new_node = self.left_rotate(node)
            if node is self.root:
                self.root = new_node
            return new_node

        return node

    @staticmethod
    def print_inorder(node):
        if node is None:
            return
        AVLTree.print_inorder(node.left)
        print node.data
        AVLTree.print_inorder(node.right)

    def insert(self, data):
        return self._insert(self.root, data)


if __name__ == "__main__":
    avl = AVLTree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.insert(25)
    avl.print_inorder(avl.root)
