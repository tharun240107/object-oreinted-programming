
import heapq   # Optional built-in heap module

# ---------------- Manual Min-Heap Implementation ----------------
class MinHeap:
    def __init__(self):
        self.heap = []

    # Get parent, left and right child indices
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # Insert element into heap
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    # Heapify upwards (for insert)
    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    # Extract minimum element (root)
    def extract_min(self):
        if not self.heap:
            print("Heap is empty! Cannot extract.")
            return None

        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    # Heapify downwards (for extract-min)
    def _heapify_down(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    # Display the heap
    def display(self):
        print("Current Min-Heap:", self.heap)


# ---------------- Heap Sort using Min-Heap ----------------
def heap_sort(arr):
    heap = MinHeap()
    for ele in arr:
        heap.insert(ele)

    sorted_list = []
    while heap.heap:
        sorted_list.append(heap.extract_min())
    return sorted_list


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Min-Heap and Priority Queue Operations ===")

    # Input elements from user
    elements = list(map(int, input("Enter elements separated by space: ").split()))
    
    # Create heap
    min_heap = MinHeap()

    # Insert elements
    for ele in elements:
        min_heap.insert(ele)

    print("\nAfter inserting elements:")
    min_heap.display()

    # Extract minimum
    print("\nExtracted Min:", min_heap.extract_min())
    print("Heap after extract-min:")
    min_heap.display()

    # Heapsort
    print("\nHeapsort result:")
    sorted_result = heap_sort(elements)
    print(sorted_result)

    # Optional: Using Python's heapq module
    print("\n=== Using Python's heapq module (for comparison) ===")
    heapq_heap = elements.copy()
    heapq.heapify(heapq_heap)
    print("Heapified list:", heapq_heap)
    print("Smallest element (heapq.heappop):", heapq.heappop(heapq_heap))
    print("Remaining heap:", heapq_heap)
