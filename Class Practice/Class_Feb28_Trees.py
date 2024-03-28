# Binary Trees

# Binary Trees include a Node, in a tree you have a root node with 2 branches.
# Left and right data

from dataclasses import dataclass

@dataclass
class Node:
    def __init__(self, data):
        self.left: None
        self.right: None
        self.data: data

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._addNode(data, self.root)

    def _addNode(self, data, node):
        if data < node.data:
            if node.left:
                self._addNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._addNode(data, node.right)
            else:
                node.right = Node(data)

    def printTree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.left)
            print(node.data, end=" -> ")
            self._view_tree(node.right)

tree = BinaryTree()
tree.add(10)
tree.add(30)
tree.add(15)
tree.add(40)
tree.add(50)

tree.printTree()
