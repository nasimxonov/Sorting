def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

lists = [5, 8, 10, 12, 15, 18]
mid_index = len(lists) // 2
mid = lists[mid_index]

x = 12

bir = lists[:mid_index]
ikki = lists[mid_index:]

print("O'rtadagi element:", mid)
print("Birinchi qism elementi:", binary_search(bir, x))
print("Ikkinchi qism elementi:", binary_search(ikki, x))
