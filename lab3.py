
# ---------------- Array-based Queue ----------------
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow! Cannot dequeue.")
            return None
        return self.queue.pop(0)

    def front(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
            return None
        return self.queue[0]

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
            return
        print("Queue elements:", self.queue)


# ---------------- Circular Queue ----------------
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        # Check for full condition
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue is full! Cannot enqueue.")
            return

        # First element insertion
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue is empty! Cannot dequeue.")
            return None

        item = self.queue[self.front]
        print(f"Dequeued: {item}")

        # Queue becomes empty
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def display(self):
        if self.front == -1:
            print("Circular Queue is empty.")
            return

        print("Circular Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Array-based Queue Operations ===")
    aq = ArrayQueue()

    # User input for queue elements
    elements = list(map(int, input("Enter elements to enqueue in array-based queue: ").split()))
    for ele in elements:
        aq.enqueue(ele)

    print("\nAfter enqueue operations:")
    aq.display()

    # Dequeue twice
    aq.dequeue()
    aq.dequeue()
    print("After two dequeue operations:")
    aq.display()

    if aq.front() is not None:
        print("Front element is:", aq.front())

    # ---------------- Circular Queue ----------------
    print("\n=== Circular Queue Operations ===")
    size = int(input("Enter size of circular queue: "))
    cq = CircularQueue(size)

    # Enqueue elements
    elements = list(map(int, input("Enter elements to enqueue in circular queue: ").split()))
    for ele in elements:
        cq.enqueue(ele)

    # Dequeue twice
    cq.dequeue()
    cq.dequeue()

    # Enqueue one more (wrap-around test)
    extra = int(input("Enter one element to enqueue (wrap-around test): "))
    cq.enqueue(extra)

    print("\nFinal state of circular queue:")
    cq.display()
