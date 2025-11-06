
# --------------------- Node Class ---------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# --------------------- Singly Linked List ---------------------
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_front(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        print(f"Deleted element from front: {self.head.data}")
        self.head = self.head.next

    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print("Linked List elements:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# --------------------- Stack Using Linked List ---------------------
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow! Cannot pop.")
            return None
        popped = self.top.data
        self.top = self.top.next
        print(f"Popped element: {popped}")
        return popped

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        print(f"Top element is: {self.top.data}")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.top is None:
            print("Stack is empty.")
            return
        temp = self.top
        print("Stack elements (top to bottom):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# --------------------- Main Program ---------------------
if __name__ == "__main__":
    print("=== Singly Linked List Operations ===")
    sll = SinglyLinkedList()

    # User input for linked list
    elements = list(map(int, input("Enter elements to insert in linked list (space-separated): ").split()))
    
    # Insert elements at end
    for ele in elements:
        sll.insert_at_end(ele)

    print("\nLinked list after insertion:")
    sll.traverse()

    # Delete from front
    sll.delete_front()
    print("After deleting front element:")
    sll.traverse()

    print("\n=== Stack Operations ===")
    stack = Stack()

    # User input for stack elements
    stack_elements = list(map(int, input("Enter elements to push into stack (space-separated): ").split()))
    for ele in stack_elements:
        stack.push(ele)

    print("\nStack after pushes:")
    stack.display()

    # Pop operation
    stack.pop()
    print("Stack after one pop:")
    stack.display()

    # Peek operation
    stack.peek()
