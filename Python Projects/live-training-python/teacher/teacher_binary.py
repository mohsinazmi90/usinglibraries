def binary_search(arr, target):
    """
    Performs binary search on a sorted list, returns the index if found, else -1
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found, elif
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Target not found


# Example usage (List must be sorted)
number = [2, 5, 8, 12, 16, 18, 23, 38, 56, 72, 91]
target_num = 23
index = binary_search(number, target_num)

if index != -1:
    print(f"Element found at {index}")
else:
    print("Element not found")
