# Program: Binary Search Tree and Traversals
# Author: Tharun (Roll No: 24328)
# Objective: Code tree traversals and BST operations (CO1, CO2)

# ---------------- Node Class ----------------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# ---------------- Binary Search Tree Class ----------------
class BST:
    def __init__(self):
        self.root = None

    # Insert a new key
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    # Search for a key
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    # Delete a key (handles leaf and one-child cases)
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        # Traverse the tree
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node found
            # Case 1: No child (leaf)
            if root.left is None and root.right is None:
                return None
            # Case 2: One child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 3: Two children
            temp = self._find_min(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)
        return root

    # Helper to find minimum value node
    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    # Inorder Traversal (Left -> Root -> Right)
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Binary Search Tree Operations ===")
    bst = BST()

    # User input for insertion
    elements = list(map(int, input("Enter elements to insert in BST (space-separated): ").split()))
    for ele in elements:
        bst.insert(ele)

    print("\nInorder traversal after insertion:")
    print(bst.inorder())

    # Search operation
    key = int(input("\nEnter element to search: "))
    node = bst.search(key)
    if node:
        print(f"Element {key} found in BST.")
    else:
        print(f"Element {key} not found in BST.")

    # Delete operation
    key = int(input("\nEnter element to delete: "))
    bst.delete(key)

    print("\nInorder traversal after deletion:")
    print(bst.inorder())
