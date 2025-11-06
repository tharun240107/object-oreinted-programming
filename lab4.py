
import time
import random

# ---------------- Insertion Sort ----------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ---------------- Merge Sort ----------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive sorting
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging process
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Sorting Algorithms: Insertion Sort & Merge Sort ===")
    user_input = list(map(int, input("Enter numbers separated by space: ").split()))

    # Display user input
    print("\nOriginal list:", user_input)

    # Insertion Sort
    arr1 = user_input.copy()
    start_time = time.time()
    insertion_sort(arr1)
    end_time = time.time()
    print("\nAfter Insertion Sort:", arr1)
    print(f"Insertion Sort Time: {(end_time - start_time):.6f} seconds")

    # Merge Sort
    arr2 = user_input.copy()
    start_time = time.time()
    merge_sort(arr2)
    end_time = time.time()
    print("\nAfter Merge Sort:", arr2)
    print(f"Merge Sort Time: {(end_time - start_time):.6f} seconds")

    # Compare with random list of 50 integers
    print("\n=== Performance Comparison on Random List of 50 Integers ===")
    random_list = [random.randint(1, 1000) for _ in range(50)]

    # Insertion Sort Timing
    arr1 = random_list.copy()
    start_time = time.time()
    insertion_sort(arr1)
    insertion_time = time.time() - start_time

    # Merge Sort Timing
    arr2 = random_list.copy()
    start_time = time.time()
    merge_sort(arr2)
    merge_time = time.time() - start_time

    print(f"Insertion Sort Time (50 random elements): {insertion_time:.6f} sec")
    print(f"Merge Sort Time (50 random elements): {merge_time:.6f} sec")

    # Efficiency summary
    if insertion_time < merge_time:
        print("\n✅ Insertion Sort was faster for this run.")
    else:
        print("\n✅ Merge Sort was faster for this run.")
