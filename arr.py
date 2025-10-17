arr = [10, 20, 30, 40, 50] 
print("Initial Array:", arr) 
print("\nTraversal of array:") 
for i in range(len(arr)): 
    print(arr[i], end=" ") 
print() 
index = 2 
element = 25 
arr.insert(index, element) 
print(f"\nAfter inserting {element} at index {index}: {arr}") 
middle_index = len(arr) // 2 
3 
 
element = 35 
arr.insert(middle_index, element) 
print(f"After inserting {element} at middle index {middle_index}: {arr}") 
index = 3 
deleted_element = arr.pop(index) 
print(f"\nAfter deleting element at index {index} ({deleted_element}): {arr}") 
middle_index = len(arr) // 2 
deleted_element = arr.pop(middle_index) 
print(f"After deleting middle element ({deleted_element}): {arr}") 
element_to_search = 40 
found = False 
for i in range(len(arr)): 
    if arr[i] == element_to_search: 
        print(f"\nElement {element_to_search} found at index {i}") 
        found = True 
        break 
if not found: 
    print(f"\nElement {element_to_search} not found in the array") 
print("\nFinal Array Traversal:") 
for i in range(len(arr)): 
    print(arr[i], end=" ") 
print()