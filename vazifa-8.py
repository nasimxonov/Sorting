def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr) // 2]
    left = [x for x in arr if x < mid]
    middle = [x for x in arr if x == mid]
    right = [x for x in arr if x > mid]
    return quick_sort(left) + middle + quick_sort(right)

lists = [5, 3, 8, 5, 9, 5]
print("Natija:", quick_sort(lists))
