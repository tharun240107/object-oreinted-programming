
def traverse(arr):
    print("Array elements:", end=" ")
    for i in arr:
        print(i, end=" ")
    print()

def insert_element(arr, index, element):
    # Insert using slicing
    arr = arr[:index] + [element] + arr[index:]
    return arr

def delete_element(arr, index):
    # Delete element at given index
    if 0 <= index < len(arr):
        arr = arr[:index] + arr[index+1:]
    else:
        print("Invalid index for deletion.")
    return arr

def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

def update_element(arr, index, new_value):
    if 0 <= index < len(arr):
        arr[index] = new_value
    else:
        print("Invalid index for update.")
    return arr


# ---------------- Main Program ----------------
# Input list from user
arr = list(map(int, input("Enter list elements separated by space: ").split()))
print("\nOriginal array:")
traverse(arr)

# Insert operation
index = int(input("\nEnter index to insert: "))
element = int(input("Enter element to insert: "))
arr = insert_element(arr, index, element)
print("After insertion:")
traverse(arr)

# Delete operation
index = int(input("\nEnter index to delete: "))
arr = delete_element(arr, index)
print("After deletion:")
traverse(arr)

# Search operation
element = int(input("\nEnter element to search: "))
pos = linear_search(arr, element)
if pos != -1:
    print(f"Element {element} found at index {pos}")
else:
    print(f"Element {element} not found")

# Update operation
index = int(input("\nEnter index to update: "))
new_value = int(input("Enter new value: "))
arr = update_element(arr, index, new_value)
print("After update:")
traverse(arr)
