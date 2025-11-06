# Program: B-Tree Implementation (Order m = 3)
# Author: Tharun (Roll No: 24328)
# Objective: Implement B-trees for indexing (CO2)

# ---------------- B-Tree Node ----------------
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t                  # Minimum degree (order)
        self.keys = []              # List of keys
        self.children = []          # Child pointers
        self.leaf = leaf            # True if node is leaf

    def __str__(self):
        return str(self.keys)


# ---------------- B-Tree ----------------
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    # Search key in the tree
    def search(self, k, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        # Key found
        if i < len(node.keys) and node.keys[i] == k:
            return node, i

        # If node is leaf, key not present
        if node.leaf:
            return None

        # Recur in the appropriate child
        return self.search(k, node.children[i])

    # Insert key into B-Tree
    def insert(self, k):
        root = self.root
        # If root is full, split it
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.insert(0, root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, k)
            self.root = new_root
        else:
            self._insert_non_full(root, k)

    # Insert into non-full node
    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    # Split child node
    def _split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)

        # Move middle key up
        parent.keys.insert(i, y.keys[t - 1])
        parent.children.insert(i + 1, z)

        # Split keys and children
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    # Traverse the tree (Inorder-like)
    def traverse(self, node=None):
        if node is None:
            node = self.root
        result = []
        i = 0
        while i < len(node.keys):
            if not node.leaf:
                result.extend(self.traverse(node.children[i]))
            result.append(node.keys[i])
            i += 1
        if not node.leaf:
            result.extend(self.traverse(node.children[i]))
        return result


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== B-Tree Implementation (Order m = 3) ===")

    # Create a B-tree of order 3
    btree = BTree(3)

    # Input elements
    elements = list(map(int, input("Enter elements to insert in B-tree: ").split()))
    for ele in elements:
        btree.insert(ele)

    print("\nB-Tree inorder traversal after insertion:")
    print(btree.traverse())

    # Search operation
    key = int(input("\nEnter key to search: "))
    result = btree.search(key)

    if result:
        node, idx = result
        print(f"Key {key} found in node: {node.keys}")
    else:
        print(f"Key {key} not found in the B-tree.")
