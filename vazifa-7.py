def quick_sort(arr, s=0):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr) // 2]
    left = [x for x in arr if x < mid]
    middle = [x for x in arr if x == mid]
    right = [x for x in arr if x > mid]
    print("  " * s + f"Mid: {mid}, Left: {left}, Middle: {middle}, Right: {right}")
    return quick_sort(left, s + 1) + middle + quick_sort(right, s + 1)

lists = [4, 9, 3, 2, 8]
print("Natija:", quick_sort(lists))
