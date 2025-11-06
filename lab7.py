# Program: Hash Table Implementation (Open Addressing - Linear Probing)
# Author: Tharun (Roll No: 24328)
# Objective: Code hash tables with collision handling (CO2)

# ---------------- Hash Table Class ----------------
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert key using linear probing
    def insert(self, key):
        index = self.hash_function(key)
        start_index = index  # To detect full table
        while self.table[index] is not None and self.table[index] != "DELETED":
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash Table is full! Cannot insert.")
                return
        self.table[index] = key
        print(f"Inserted {key} at index {index}")

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
            if index == start_index:
                break
        return -1

    # Delete a key
    def delete(self, key):
        index = self.search(key)
        if index == -1:
            print(f"Key {key} not found for deletion.")
        else:
            self.table[index] = "DELETED"
            print(f"Deleted key {key} from index {index}")

    # Display hash table contents
    def display(self):
        print("\nHash Table contents:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Hash Table Implementation (Linear Probing) ===")

    # Input table size
    size = int(input("Enter size of hash table: "))
    ht = HashTable(size)

    # Insert elements
    keys = list(map(int, input("Enter keys to insert (space-separated): ").split()))
    for key in keys:
        ht.insert(key)

    print("\nAfter insertion:")
    ht.display()

    # Search operation
    key = int(input("\nEnter key to search: "))
    index = ht.search(key)
    if index != -1:
        print(f"Key {key} found at index {index}")
    else:
        print(f"Key {key} not found in table.")

    # Delete operation
    key = int(input("\nEnter key to delete: "))
    ht.delete(key)

    # Final table after all operations
    print("\n=== Final Hash Table After All Operations ===")
    ht.display()
