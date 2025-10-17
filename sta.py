# Stack implementation using Python list (array)
class StackArray:
    def __init__(self):
        self.stack = []

    # Push element
    def push(self, data):
        self.stack.append(data)

    # Pop element
    def pop(self):
        if not self.stack:
            print("Stack is empty!")
            return None
        return self.stack.pop()

    # Peek top element
    def peek(self):
        if not self.stack:
            print("Stack is empty!")
            return None
        return self.stack[-1]

    # Length of stack
    def length(self):
        return len(self.stack)

    # Print stack
    def display(self):
        print("Stack (top -> bottom):", self.stack[::-1])


# ------------------ DEMO ------------------
stack_arr = StackArray()
stack_arr.push(10)
stack_arr.push(20)
stack_arr.push(30)
print("Array Stack after pushes:")
stack_arr.display()

print("Peek top element:", stack_arr.peek())
print("Pop top element:", stack_arr.pop())
print("Length of stack:", stack_arr.length())
print("Stack after pop:")
stack_arr.display()
