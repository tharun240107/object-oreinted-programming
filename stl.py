# Node class for Linked List Stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack implementation using linked list
class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    # Push element
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # Pop element
    def pop(self):
        if not self.top:
            print("Stack is empty!")
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    # Peek top element
    def peek(self):
        if not self.top:
            print("Stack is empty!")
            return None
        return self.top.data

    # Length of stack
    def length(self):
        return self.size

    # Print stack
    def display(self):
        temp = self.top
        print("Stack (top -> bottom):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ------------------ DEMO ------------------
stack_ll = StackLinkedList()
stack_ll.push(100)
stack_ll.push(200)
stack_ll.push(300)
print("\nLinked List Stack after pushes:")
stack_ll.display()

print("Peek top element:", stack_ll.peek())
print("Pop top element:", stack_ll.pop())
print("Length of stack:", stack_ll.length())
print("Stack after pop:")
stack_ll.display()
