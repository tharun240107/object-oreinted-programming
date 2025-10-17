import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    # Insert element (priority, value)
    def insert(self, priority, value):
        heapq.heappush(self.heap, (priority, value))

    # Delete element with highest priority (lowest number)
    def delete(self):
        if not self.heap:
            print("Priority Queue is empty!")
            return None
        return heapq.heappop(self.heap)

    # Peek at top element
    def peek(self):
        if not self.heap:
            print("Priority Queue is empty!")
            return None
        return self.heap[0]

    # Display all elements
    def display(self):
        print("Priority Queue (priority, value):", self.heap)


# ------------------ DEMO ------------------
pq = PriorityQueue()
pq.insert(3, "Task3")
pq.insert(1, "Task1")
pq.insert(2, "Task2")

print("After insertion:")
pq.display()

print("Deleted element:", pq.delete())
print("After deletion:")
pq.display()
print("Peek:", pq.peek())
