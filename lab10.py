# Program: Dijkstra’s Algorithm & Bloom Filter Implementation
# Author: Tharun (Roll No: 24328)
# Objective: Implement shortest path algorithm and advanced data structure (CO2, CO4)

import heapq
import hashlib

# ---------------- Dijkstra’s Algorithm ----------------
class Graph:
    def __init__(self):
        self.graph = {}  # adjacency list: {node: [(neighbor, weight), ...]}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # undirected graph

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, node)

        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)

            # Skip if we already found a shorter path
            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# ---------------- Bloom Filter Implementation ----------------
class BloomFilter:
    def __init__(self, size=20, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        """Generate multiple hashes using hashlib"""
        hashes = []
        for i in range(self.hash_count):
            # Create a different hash each time by salting with index
            hash_val = int(hashlib.sha256((item + str(i)).encode()).hexdigest(), 16)
            hashes.append(hash_val % self.size)
        return hashes

    def add(self, item):
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1
        print(f"Inserted '{item}' into Bloom filter.")

    def check(self, item):
        for hash_val in self._hashes(item):
            if self.bit_array[hash_val] == 0:
                return False
        return True

    def display(self):
        print("Bloom Filter bit array:", self.bit_array)


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Dijkstra’s Algorithm and Bloom Filter ===")

    # ----------- Dijkstra’s Algorithm -----------
    print("\n--- Dijkstra’s Shortest Path ---")
    g = Graph()

    # Input graph edges
    print("Enter edges in format (A-B:weight). Type 'done' when finished:")
    while True:
        edge_input = input()
        if edge_input.lower() == "done":
            break
        if "-" in edge_input and ":" in edge_input:
            u_v, w = edge_input.split(":")
            u, v = u_v.split("-")
            g.add_edge(u.strip(), v.strip(), int(w.strip()))

    start_node = input("Enter start node for Dijkstra’s: ").strip()
    distances = g.dijkstra(start_node)

    print(f"\nShortest distances from {start_node}:")
    for node, dist in distances.items():
        print(f"{start_node} → {node} = {dist}")

    # ----------- Bloom Filter -----------
    print("\n--- Bloom Filter Implementation ---")
    bf = BloomFilter(size=20, hash_count=3)

    # Insert elements
    elements = input("Enter elements to insert into Bloom filter (space-separated): ").split()
    for elem in elements:
        bf.add(elem)

    bf.display()

    # Query elements
    queries = input("\nEnter elements to check membership (space-separated): ").split()
    for q in queries:
        if bf.check(q):
            print(f"'{q}' is possibly in the set (might be a false positive).")
        else:
            print(f"'{q}' is definitely NOT in the set.")
