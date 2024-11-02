def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    a = arr[len(arr) // 2]
    left = [x for x in arr if x < a]
    middle = [x for x in arr if x == a]
    right = [x for x in arr if x > a]
    return quick_sort(left) + middle + quick_sort(right)

lists = [3, 6, 8, 10, 1, 2, 1]
print("Natija:", quick_sort(lists))
