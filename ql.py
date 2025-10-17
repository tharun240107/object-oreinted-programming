# Node class for Linked List Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue implementation using linked list
class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # Enqueue
    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:  # Empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    # Dequeue
    def dequeue(self):
        if not self.front:
            print("Queue is empty!")
            return None
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return data

    # Search element
    def search(self, data):
        temp = self.front
        index = 0
        while temp:
            if temp.data == data:
                return index
            temp = temp.next
            index += 1
        return -1

    # Size of queue
    def length(self):
        return self.size

    # Traverse
    def traverse(self):
        temp = self.front
        print("Queue (front -> rear):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ------------------ DEMO ------------------
queue_ll = QueueLinkedList()
queue_ll.enqueue(100)
queue_ll.enqueue(200)
queue_ll.enqueue(300)
print("\nLinked List Queue after enqueues:")
queue_ll.traverse()

print("Dequeue element:", queue_ll.dequeue())
print("Queue after dequeue:")
queue_ll.traverse()

print("Search 200 in queue:", queue_ll.search(200))
print("Size of queue:", queue_ll.length())
