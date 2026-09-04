def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


arr = [10, 20, 30, 40, 50, 60, 70]
key = int(input("Enter element to search: "))

result = binary_search(arr, key, 0, len(arr) - 1)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")