# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # ------------------ INSERTION OPERATIONS ------------------

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    # Insert at specific index (0-based)
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            if not temp:
                print("Index out of range")
                return
            temp = temp.next
        new_node.next = temp.next
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
        temp.next = new_node

    # Insert before a given element
    def insert_before(self, target, data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == target:
            self.insert_at_beginning(data)
            return
        temp = self.head
        while temp.next and temp.next.data != target:
            temp = temp.next
        if not temp.next:
            print(f"Element {target} not found.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # ------------------ DELETION OPERATIONS ------------------

    # Delete at beginning
    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next

    # Delete at end
    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete at specific index
    def delete_at_index(self, index):
        if not self.head:
            return
        if index == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(index - 1):
            if not temp.next:
                print("Index out of range")
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    # Delete after a given element
    def delete_after(self, target):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if temp and temp.next:
            temp.next = temp.next.next

    # Delete before a given element
    def delete_before(self, target):
        if not self.head or not self.head.next:
            return
        if self.head.next.data == target:
            self.delete_at_beginning()
            return
        prev = None
        temp = self.head
        while temp.next and temp.next.data != target:
            prev = temp
            temp = temp.next
        if temp.next:
            prev.next = temp.next

    # ------------------ OTHER OPERATIONS ------------------

    # Traverse and print all elements
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Get size of the list
    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Sort the linked list
    def sort_list(self):
        if not self.head:
            return
        temp1 = self.head
        while temp1:
            temp2 = temp1.next
            while temp2:
                if temp1.data > temp2.data:
                    temp1.data, temp2.data = temp2.data, temp1.data
                temp2 = temp2.next
            temp1 = temp1.next


# ------------------ MAIN PROGRAM ------------------

ll = SinglyLinkedList()

# Insertion operations
ll.insert_at_end(50)
ll.insert_at_beginning(20)
ll.insert_at_end(70)
ll.insert_at_index(1, 30)
ll.insert_after(30, 40)
ll.insert_before(50, 45)

print("After Insertions:")
ll.traverse()

# Deletion operations
ll.delete_at_beginning()
ll.delete_at_end()
ll.delete_at_index(2)
ll.delete_after(30)
ll.delete_before(70)

print("\nAfter Deletions:")
ll.traverse()

# Sorting
ll.sort_list()
print("\nAfter Sorting:")
ll.traverse()

# Size of the list
print(f"\nSize of the list: {ll.size()}")

print("\nFinal Linked List Elements after all operations:")
ll.traverse()
