class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    # Check if queue is full
    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    # Check if queue is empty
    def is_empty(self):
        return self.front == -1

    # Enqueue (insert at rear)
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = data

    # Dequeue (delete from front)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:  # Only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return data

    # Get current size of queue
    def size(self):
        if self.is_empty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.max_size - (self.front - self.rear - 1)

    # Traverse / print all elements
    def traverse(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Circular Queue elements (front -> rear):", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.max_size
        print()


# ------------------ DEMO ------------------
cq = CircularQueue(5)

# Enqueue elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
print("After enqueues:")
cq.traverse()

# Dequeue element
print("Dequeued element:", cq.dequeue())
print("After dequeue:")
cq.traverse()

# Current size
print("Current size of circular queue:", cq.size())

# Enqueue more elements to show wrap-around
cq.enqueue(50)
print("After enqueue 50:")
cq.traverse()
