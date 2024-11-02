def max_count(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == len(arr) - 1 or arr[mid] > arr[mid + 1]:
            return arr[mid]
        left = mid + 1
    return arr[0]

lists = [1, 2, 3, 4, 5, 6]
print("Natija:", max_count(lists))
