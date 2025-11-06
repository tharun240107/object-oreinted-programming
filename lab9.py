# Program: Graph Representation and Traversals (DFS & BFS)
# Author: Tharun (Roll No: 24328)
# Objective: Implement graph representations and traversals (CO1, CO2)

from collections import deque

# ---------------- Graph Class ----------------
class Graph:
    def __init__(self):
        # Adjacency list representation
        self.graph = {}

    # Add node to graph
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Add edge (undirected graph)
    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_node(u)
        if v not in self.graph:
            self.add_node(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Display adjacency list
    def display(self):
        print("\nAdjacency List Representation:")
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    # Depth-First Search (DFS)
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Breadth-First Search (BFS)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Graph Representation and Traversals (DFS & BFS) ===")

    g = Graph()

    # Input nodes
    nodes = input("Enter graph nodes (space-separated): ").split()
    for node in nodes:
        g.add_node(node)

    # Input edges
    print("Enter edges (format: A-B), type 'done' to stop:")
    while True:
        edge = input()
        if edge.lower() == "done":
            break
        if "-" in edge:
            u, v = edge.split("-")
            g.add_edge(u.strip(), v.strip())

    # Display adjacency list
    g.display()

    # Choose start node for traversal
    start_node = input("\nEnter start node for traversals: ").strip()

    print("\nDFS Traversal:")
    g.dfs(start_node)

    print("\nBFS Traversal:")
    g.bfs(start_node)
