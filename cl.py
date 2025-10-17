# Node class for Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # ------------------ INSERTION OPERATIONS ------------------

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    # Insert at specific index (0-based)
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        count = 0
        while count < index - 1:
            temp = temp.next
            count += 1
            if temp == self.head:
                print("Index out of range.")
                return
        new_node.next = temp.next
        temp.next = new_node

    # Insert after a given element
    def insert_after(self, target, data):
        temp = self.head
        while True:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"Element {target} not found.")

    # Insert before a given element
    def insert_before(self, target, data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == target:
            self.insert_at_beginning(data)
            return
        prev = self.head
        temp = self.head.next
        while temp != self.head:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp
                prev.next = new_node
                return
            prev = temp
            temp = temp.next
        print(f"Element {target} not found.")

    # ------------------ DELETION OPERATIONS ------------------

    # Delete at beginning
    def delete_at_beginning(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    # Delete at end
    def delete_at_end(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        prev = None
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head

    # Delete at specific index
    def delete_at_index(self, index):
        if not self.head:
            return
        if index == 0:
            self.delete_at_beginning()
            return
        prev = self.head
        temp = self.head.next
        count = 1
        while temp != self.head and count < index:
            prev = temp
            temp = temp.next
            count += 1
        if temp == self.head:
            print("Index out of range.")
            return
        prev.next = temp.next

    # Delete after a given element
    def delete_after(self, target):
        temp = self.head
        while True:
            if temp.data == target:
                if temp.next == self.head:
                    temp.next = temp.next.next
                else:
                    temp.next = temp.next.next
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"Element {target} not found.")

    # Delete before a given element
    def delete_before(self, target):
        if not self.head or self.head.next == self.head:
            return
        prev = None
        curr = self.head
        nxt = curr.next
        if nxt.data == target:
            self.delete_at_beginning()
            return
        while nxt != self.head:
            if nxt.data == target:
                if prev:
                    prev.next = nxt
                return
            prev = curr
            curr = nxt
            nxt = nxt.next
        print(f"Element {target} not found.")

    # ------------------ OTHER OPERATIONS ------------------

    # Traverse and print
    def traverse(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    # Size of list
    def size(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    # Sort the circular linked list (ascending)
    def sort_list(self):
        if not self.head or self.head.next == self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next != self.head:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                    swapped = True
                temp = temp.next


# ------------------ MAIN PROGRAM ------------------

cll = CircularLinkedList()

# Insertions
cll.insert_at_end(50)
cll.insert_at_beginning(20)
cll.insert_at_end(80)
cll.insert_at_index(1, 30)
cll.insert_after(30, 40)
cll.insert_before(50, 45)

print("After Insertions:")
cll.traverse()

# Deletions
cll.delete_at_beginning()
cll.delete_at_end()
cll.delete_at_index(2)
cll.delete_after(30)
cll.delete_before(80)

print("\nAfter Deletions:")
cll.traverse()

# Sorting
cll.sort_list()
print("\nAfter Sorting:")
cll.traverse()

# Size
print(f"\nSize of the list: {cll.size()}")

print("\nFinal Circular Linked List Elements after all operations:")
cll.traverse()
