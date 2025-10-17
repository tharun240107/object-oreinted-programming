# Queue implementation using Python list (array)
class QueueArray:
    def __init__(self):
        self.queue = []

    # Enqueue (insert at rear)
    def enqueue(self, data):
        self.queue.append(data)

    # Dequeue (remove from front)
    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
            return None
        return self.queue.pop(0)

    # Search element
    def search(self, data):
        for i, val in enumerate(self.queue):
            if val == data:
                return i
        return -1

    # Size of queue
    def size(self):
        return len(self.queue)

    # Traverse
    def traverse(self):
        print("Queue (front -> rear):", self.queue)


# ------------------ DEMO ------------------
queue_arr = QueueArray()
queue_arr.enqueue(10)
queue_arr.enqueue(20)
queue_arr.enqueue(30)
print("Array Queue after enqueues:")
queue_arr.traverse()

print("Dequeue element:", queue_arr.dequeue())
print("Queue after dequeue:")
queue_arr.traverse()

print("Search 20 in queue:", queue_arr.search(20))
print("Size of queue:", queue_arr.size())
