# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ------------------ INSERTION OPERATIONS ------------------

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Insert at specific index (0-based)
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            if not temp:
                print("Index out of range.")
                return
            temp = temp.next
        if not temp:
            print("Index out of range.")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    # Insert after a given element
    def insert_after(self, target, data):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if not temp:
            print(f"Element {target} not found.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    # Insert before a given element
    def insert_before(self, target, data):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if not temp:
            print(f"Element {target} not found.")
            return
        new_node = Node(data)
        new_node.next = temp
        new_node.prev = temp.prev
        if temp.prev:
            temp.prev.next = new_node
        else:
            self.head = new_node
        temp.prev = new_node

    # ------------------ DELETION OPERATIONS ------------------

    # Delete at beginning
    def delete_at_beginning(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    # Delete at end
    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    # Delete at specific index
    def delete_at_index(self, index):
        if not self.head:
            return
        if index == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(index):
            if not temp:
                print("Index out of range.")
                return
            temp = temp.next
        if not temp:
            print("Index out of range.")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    # Delete after a given element
    def delete_after(self, target):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if temp and temp.next:
            to_delete = temp.next
            temp.next = to_delete.next
            if to_delete.next:
                to_delete.next.prev = temp

    # Delete before a given element
    def delete_before(self, target):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if temp and temp.prev:
            to_delete = temp.prev
            if to_delete.prev:
                to_delete.prev.next = temp
                temp.prev = to_delete.prev
            else:
                self.head = temp
                temp.prev = None

    # ------------------ OTHER OPERATIONS ------------------

    # Traverse forward
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Get size of list
    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Sort the list (ascending order)
    def sort_list(self):
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                    swapped = True
                temp = temp.next


# ------------------ MAIN PROGRAM ------------------

dll = DoublyLinkedList()

# Insertion operations
dll.insert_at_end(50)
dll.insert_at_beginning(20)
dll.insert_at_end(80)
dll.insert_at_index(1, 30)
dll.insert_after(30, 40)
dll.insert_before(50, 45)

print("After Insertions:")
dll.traverse()

# Deletion operations
dll.delete_at_beginning()
dll.delete_at_end()
dll.delete_at_index(2)
dll.delete_after(30)
dll.delete_before(80)

print("\nAfter Deletions:")
dll.traverse()

# Sorting
dll.sort_list()
print("\nAfter Sorting:")
dll.traverse()

# Size of the list
print(f"\nSize of the list: {dll.size()}")

print("\nFinal Doubly Linked List Elements after all operations:")
dll.traverse()
