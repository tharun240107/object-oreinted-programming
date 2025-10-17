# Node class for Binary Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insertion (manual linking)
    def insert_root(self, key):
        self.root = Node(key)

    def insert_left(self, parent, key):
        parent.left = Node(key)

    def insert_right(self, parent, key):
        parent.right = Node(key)

    # Traversal (for checking)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)


# ------------------ DEMO ------------------
tree = BinaryTree()
tree.insert_root(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

print("Inorder Traversal of Binary Tree:")
tree.inorder(tree.root)
